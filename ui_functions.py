from main import *

class Ui_Functions(ui_windows):

    def depart_animation(self, max_height):
        height = self.ui.set_time_frame.geometry().height()
        max_extend = max_height
        standard = 0

        if height == standard:
            height_extended = max_extend
            self.ui.find_path_btn.hide()
            self.ui.start_path_btn.hide()
            show = False
        
        else:
            height_extended = standard
            show = True
        
        self.animation = QPropertyAnimation(self.ui.set_time_frame, b"size")
        self.animation.setDuration(400)
        self.animation.setStartValue(QSize(171, height))
        self.animation.setEndValue(QSize(171, height_extended))
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
        self.animation.finished.connect(lambda: self.ui.find_path_btn.show() if show else self.ui.find_path_btn.hide())
    
    def preferences_animation(self, max_width):
        width = self.ui.preferences_frame.geometry().width()
        x = self.ui.preferences_frame.geometry().topLeft().x()
        max_extend = max_width
        standard = 0

        if width == standard:
            width_extended = max_extend
            x_extend = 1310
            self.ui.find_path_btn.hide()
            self.ui.time_frame.hide()
            self.ui.start_path_btn.hide()
            self.ui.set_time_frame.setGeometry(1310,200,171,0)
            self.ui.change_time_btn.setDisabled(True)
            show = False
        
        else:
            width_extended = standard
            x_extend = 1551
            show = True
            self.ui.change_time_btn.setDisabled(False)
        
        self.preference_animation = QPropertyAnimation(self.ui.preferences_frame, b"geometry")
        self.preference_animation.setDuration(400)
        self.preference_animation.setStartValue(QRect(x, 200, width,221))
        self.preference_animation.setEndValue(QRect(x_extend, 200, width_extended, 221))
        self.preference_animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.preference_animation.start()
        self.preference_animation.finished.connect(lambda: self.ui.find_path_btn.show() if show else self.ui.find_path_btn.hide())
    
    def depart_now(self, time):
        self.set_time = time
        self.ui.set_time_frame.setGeometry(1310,200,171,0)
        self.ui.change_time_btn.setText(f"{self.set_time} ▼")
        self.ui.time_frame.hide()
        self.ui.find_path_btn.show()
    
    def change_time(self):
        self.ui.set_time_frame.setGeometry(1310,200,171,0)
        self.ui.time_frame.show()
    
    def destination_function(self, destination):
        if not self.destination:
            self.ending_point = destination[3]
            self.ui.depaarture_line.setText(f"  {destination[2]}")
            self.ui.depart_line.setPlaceholderText("  Başlangıç noktası seç")
            self.set_destination_style(self.nodes_destination_style, self.previous_start)
            destination[1].setStyleSheet(self.selected_destination_style)
            self.previous_end = destination[1]
            self.selected_destination = destination
        
        else:
            self.starting_point = destination[3]
            self.ui.depart_line.setText(f"  {destination[2]}")
            self.set_destination_style(self.nodes_start_style, self.previous_end)
            destination[1].setStyleSheet(self.selected_start_style)
            self.previous_start = destination[1]
            self.selected_start = destination
