#!/usr/bin/env python3

from migen import *
from migen.genlib.io import CRG
from migen.genlib.cdc import MultiReg

import nexys4ddr as tarjeta
#import c4e6e10 as tarjeta

from litex.soc.integration.soc_core import *
from litex.soc.integration.builder import *
from litex.soc.interconnect.csr import *
from litex.soc.integration.soc import *

from litex.soc.cores import gpio
from module import rgbled
from module import sevensegment
from module import camara
from module import vgacontroller
from module import pwm
from module import infrarrojo
from module import ultrasonido
from module import motores

# BaseSoC ------------------------------------------------------------------------------------------

class BaseSoC(SoCCore):
	def __init__(self):
		platform = tarjeta.Platform()
		# SoC with CPU
		SoCCore.__init__(self, platform,
 			cpu_type="picorv32",
#			cpu_type="vexriscv",
			clk_freq=100e6,
			integrated_rom_size=0x6000,
			integrated_main_ram_size=16*1024)
			
			
		#pwm
		platform.add_source("module/verilog/pwm.v")

		#Camara
		platform.add_source("module/verilog/Analyzer.v")
		platform.add_source("module/verilog/test_cam.v")
		platform.add_source("module/verilog/cam_read.v")
		platform.add_source("module/verilog/buffer_ram_dp.v")
		platform.add_source("module/verilog/clk24_25_nexys4.v")

		#infrarrojo
		platform.add_source("module/verilog/infrarrojo.v")
		
		#ultrasonido
		platform.add_source("module/verilog//ultrasonido/bloqueultrasonido.v")
		platform.add_source("module/verilog//ultrasonido/contador.v")
		platform.add_source("module/verilog//ultrasonido/divisor.v")
		platform.add_source("module/verilog//ultrasonido/divisorfrec.v")
		platform.add_source("module/verilog//ultrasonido/divisorfrecd.v")
		platform.add_source("module/verilog//ultrasonido/divisorfrecgen.v")
		platform.add_source("module/verilog//ultrasonido/divisorfrecme.v")
		platform.add_source("module/verilog//ultrasonido/genpulsos.v")
		platform.add_source("module/verilog//ultrasonido/maquinadeestados.v")
		platform.add_source("module/verilog//ultrasonido/meultrasonido.v")
		platform.add_source("module/verilog//ultrasonido/ultrasonido.v")
		
		#Motores
		platform.add_source("module/verilog/Motor.v")
        	
		# Clock Reset Generation
		self.submodules.crg = CRG(platform.request("clk"), ~platform.request("cpu_reset"))

		# Leds
		SoCCore.add_csr(self,"leds")
		user_leds = Cat(*[platform.request("led", i) for i in range(10)])
		self.submodules.leds = gpio.GPIOOut(user_leds)
		
		# Switchs
		SoCCore.add_csr(self,"switchs")
		user_switchs = Cat(*[platform.request("sw", i) for i in range(8)])
		self.submodules.switchs = gpio.GPIOIn(user_switchs)
		
		# Buttons
		SoCCore.add_csr(self,"buttons")
		user_buttons = Cat(*[platform.request("btn%c" %c) for c in ['c','r','l']])
		self.submodules.buttons = gpio.GPIOIn(user_buttons)
		
		# 7segments Display
		SoCCore.add_csr(self,"display")
		display_segments = Cat(*[platform.request("display_segment", i) for i in range(8)])
		display_digits = Cat(*[platform.request("display_digit", i) for i in range(8)])
		self.submodules.display = sevensegment.SevenSegment(display_segments,display_digits)

		# RGB leds
		SoCCore.add_csr(self,"ledRGB_1")
		self.submodules.ledRGB_1 = rgbled.RGBLed(platform.request("ledRGB",1))
		
		SoCCore.add_csr(self,"ledRGB_2")
		self.submodules.ledRGB_2 = rgbled.RGBLed(platform.request("ledRGB",2))

		# camara
		SoCCore.add_csr(self, "camara_cntrl")
		# SoCCore.add_interrupt(self,"camara_cntrl")
		cam_data_in = Cat(*[platform.request("CAM_px_data", i) for i in range(8)])
		self.submodules.camara_cntrl = camara.Camara(platform.request("CAM_xclk"), platform.request("CAM_pclk"),
													 platform.request("CAM_href"), platform.request("CAM_vsync"),
													 cam_data_in)


		#pwm
		SoCCore.add_csr(self,"pwm_cntrl")
		self.submodules.pwm_cntrl = pwm.Pwm(platform.request("pwm"))
		
		#ultrasonido
		SoCCore.add_csr(self,"ultra_cntrl")
		self.submodules.ultra_cntrl = ultrasonido.Ultra(platform.request("trigg"),platform.request("ECHO"))
		
		#infrarrojo
		SoCCore.add_csr(self,"infra_cntrl")
		infras_in = Cat(*[platform.request("infras", i) for i in range(5)])
		self.submodules.infra_cntrl = infrarrojo.Infrarrojo(infras_in)

		#motores
		SoCCore.add_csr(self,"motor_cntrl")
		motor_out = Cat(*[platform.request("pin", i) for i in range(4)])
		self.submodules.motor_cntrl = motores.Motores(motor_out)
		
		# VGA
		SoCCore.add_csr(self,"vga_cntrl")
		vga_red = Cat(*[platform.request("vga_red", i) for i in range(4)])
		vga_green = Cat(*[platform.request("vga_green", i) for i in range(4)])
		vga_blue = Cat(*[platform.request("vga_blue", i) for i in range(4)])
		self.submodules.vga_cntrl = vgacontroller.VGAcontroller(platform.request("hsync"),platform.request("vsync"), vga_red, vga_green, vga_blue)

# Build --------------------------------------------------------------------------------------------
if __name__ == "__main__":
	builder = Builder(BaseSoC())
	builder.build()

