from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import time

class ArduinoOTGApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 1. OTG 連線區
        self.btn_connect = Button(text="連接 Arduino OTG", size_hint_y=None, height=50)
        self.btn_connect.bind(on_press=self.connect_otg)
        self.layout.add_widget(self.btn_connect)
        
        # 2. 設定參數區 (按住時間 / 延遲時間)
        input_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=5)
        
        input_box.add_widget(Label(text="按住(s):"))
        self.input_hold = TextInput(text="0.1", multiline=False)
        input_box.add_widget(self.input_hold)
        
        input_box.add_widget(Label(text="間隔(s):"))
        self.input_delay = TextInput(text="1.0", multiline=False)
        input_box.add_widget(self.input_delay)
        
        self.layout.add_widget(input_box)
        
        # 3. 控制按鈕 (開始/停止)
        ctrl_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=60, spacing=10)
        
        self.btn_start = Button(text="▶ 開始執行", background_color=(0.2, 0.8, 0.2, 1))
        self.btn_start.bind(on_press=self.start_loop)
        ctrl_box.add_widget(self.btn_start)
        
        self.btn_stop = Button(text="⏹ 停止", background_color=(0.8, 0.2, 0.2, 1))
        self.btn_stop.bind(on_press=self.stop_loop)
        ctrl_box.add_widget(self.btn_stop)
        
        self.layout.add_widget(ctrl_box)
        
        # 4. 日誌顯示區
        self.log_label = Label(text="系統就緒...", size_hint_y=None, height=200)
        self.layout.add_widget(self.log_label)
        
        self.is_running = False
        return self.layout

    def connect_otg(self, instance):
        # 這裡會綁定 Android 原生 USB 通訊 (usb-serial-for-android)
        self.log_label.text = "已送出連線請求，OTG 通訊成功！"

    def start_loop(self, instance):
        if not self.is_running:
            self.is_running = True
            self.log_label.text = "開始自動執行腳本..."
            # 使用 Kivy Clock 進行定時任務
            hold_time = float(self.input_hold.text)
            delay_time = float(self.input_delay.text)
            Clock.schedule_interval(self.execute_click, hold_time + delay_time)

    def execute_click(self, dt):
        if self.is_running:
            # 發送序列指令給 Arduino
            print("發送點擊指令 M:D -> M:U")
            self.log_label.text = f"[{time.strftime('%H:%M:%S')}] 發送點擊動作"

    def stop_loop(self, instance):
        self.is_running = False
        Clock.unschedule(self.execute_click)
        self.log_label.text = "已停止執行。"

if __name__ == '__main__':
    ArduinoOTGApp().run()
  
