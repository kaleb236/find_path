import sys
from PyQt5.QtWidgets import QApplication
import math
import random
from user import Ui_MainWindow
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ui_functions import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from datetime import datetime

class ui_windows(QMainWindow):
    clicked=pyqtSignal()
    destination_click = pyqtSignal()
    def __init__(self):
        super(ui_windows, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #########INITIAL HIDES#########
        self.ui.time_frame.hide()
        self.ui.start_btn.hide()
        self.ui.trafikli_frame.hide()
        self.ui.trafiksiz_frame.hide()
        self.ui.filtered_label.hide()
        self.ui.animation_frame.hide()
        self.ui.start_path_btn.hide()

        self.ui.depart_line.installEventFilter(self)
        self.clicked.connect(self.set_destination_true)

        self.ui.depaarture_line.installEventFilter(self)
        self.destination_click.connect(self.set_destination_false)

        ##########INITIAL VARIABLES###########
        self.set_time = "Şimdi ayrıl"
        self.destination = False
        self.selected_destination = False
        self.selected_start = False
        self.filter = False
        self.reversable = True

        self.choose_time = []
        self.choose_way = []
        self.choise = 0
        self.cnt = 0
        self.add = +1
        self.set_hours = 0

        self.starting_point = 0
        self.ending_point = 0

        self.red = QColor(200,0,0,255)
        self.blue = QColor(0,0,200,255)

        self.nodes_destination_style = """
        QPushButton:hover{
            image: url(:/images/images/goto.png);
        }
        """
        self.nodes_start_style = """
        QPushButton:hover{
            image: url(:/images/images/current.png);
        }
        """

        self.selected_destination_style = """
        QPushButton{
            image: url(:/images/images/goto.png);
        }
        QPushButton:hover{
            image: url(:/images/images/goto.png);
        }
        """
        self.selected_start_style = """
        QPushButton{
            image: url(:/images/images/current.png);
        }
        QPushButton:hover{
            image: url(:/images/images/current.png);
        }
        """

        self.pen = QPen(QBrush(QColor(0,0,200,255)), 4)

        self.starting = 0
        self.ending = 0

        self.previous_start = 0
        self.previous_end = 0

        self.ui.start_frame.hide()

        self.graph = {}

        self.added = 0
        self.node_1 = [self.ui.node_1.geometry().center().x() + self.added, self.ui.node_1.geometry().center().y()]
        self.node_2 = [self.ui.node_2.geometry().center().x() + self.added, self.ui.node_2.geometry().center().y()]
        self.node_3 = [self.ui.node_3.geometry().center().x() + self.added, self.ui.node_3.geometry().center().y()]
        self.node_4 = [self.ui.node_4.geometry().center().x() + self.added, self.ui.node_4.geometry().center().y()]
        self.node_5 = [self.ui.node_5.geometry().center().x() + self.added, self.ui.node_5.geometry().center().y()]
        self.node_6 = [self.ui.node_6.geometry().center().x() + self.added, self.ui.node_6.geometry().center().y()]
        self.node_7 = [self.ui.node_7.geometry().center().x() + self.added, self.ui.node_7.geometry().center().y()]
        self.node_8 = [self.ui.node_8.geometry().center().x() + self.added, self.ui.node_8.geometry().center().y()]
        self.node_9 = [self.ui.node_9.geometry().center().x() + self.added, self.ui.node_9.geometry().center().y()]
        self.node_10 = [self.ui.node_10.geometry().center().x() + self.added, self.ui.node_10.geometry().center().y()]
        self.node_11 = [self.ui.node_11.geometry().center().x() + self.added, self.ui.node_11.geometry().center().y()]
        self.node_12 = [self.ui.node_12.geometry().center().x() + self.added, self.ui.node_12.geometry().center().y()]

        for i in range(24):
            k = str(i)
            if len(k) < 2:
                k = "0"+k
            self.ui.hours_combo.addItem(k)
        
        self.ui.min_combo.addItems(["00", "15", "30", "45"])

        self.ui.node_1.clicked.connect(lambda: Ui_Functions.destination_function(self, self.nodes_dict[1]))
        self.ui.node_2.clicked.connect(lambda: Ui_Functions.destination_function(self, self.nodes_dict[2]))
        self.ui.node_3.clicked.connect(lambda: Ui_Functions.destination_function(self, self.nodes_dict[3]))
        self.ui.node_4.clicked.connect(lambda: Ui_Functions.destination_function(self, self.nodes_dict[4]))
        self.ui.node_5.clicked.connect(lambda: Ui_Functions.destination_function(self, self.nodes_dict[5]))
        self.ui.node_6.clicked.connect(lambda: Ui_Functions.destination_function(self, self.nodes_dict[6]))
        self.ui.node_7.clicked.connect(lambda: Ui_Functions.destination_function(self, self.nodes_dict[7]))
        self.ui.node_8.clicked.connect(lambda: Ui_Functions.destination_function(self, self.nodes_dict[8]))
        self.ui.node_9.clicked.connect(lambda: Ui_Functions.destination_function(self, self.nodes_dict[9]))
        self.ui.node_10.clicked.connect(lambda: Ui_Functions.destination_function(self, self.nodes_dict[10]))
        self.ui.node_11.clicked.connect(lambda: Ui_Functions.destination_function(self, self.nodes_dict[11]))
        self.ui.node_12.clicked.connect(lambda: Ui_Functions.destination_function(self, self.nodes_dict[12]))

        

        #########SET DIRECTIONS BUTTONS########
        self.ui.change_time_btn.clicked.connect(lambda: Ui_Functions.depart_animation(self, 81))
        self.ui.depart_now.clicked.connect(lambda: Ui_Functions.depart_now(self, "Şimdi ayrıl"))
        self.ui.ok_btn.clicked.connect(lambda: Ui_Functions.depart_now(self, f"{self.ui.hours_combo.currentText()} : {self.ui.min_combo.currentText()}"))
        self.ui.cancel_btn.clicked.connect(lambda: Ui_Functions.depart_now(self, self.set_time))
        self.ui.change_time.clicked.connect(lambda: Ui_Functions.change_time(self))

        ##########PREFERENCES BUTTON ACTIONS###########
        self.ui.preferences_btn.clicked.connect(lambda: Ui_Functions.preferences_animation(self, 241))
        self.ui.close_btn.clicked.connect(lambda: Ui_Functions.preferences_animation(self, 241))
        self.ui.reverse_btn.clicked.connect(self.reverse)
        self.ui.find_path_btn.clicked.connect(self.find_path)
        self.ui.find_path_btn_2.clicked.connect(self.find_path)

        self.ui.start_path_btn.clicked.connect(self.path_animation)
        
        self.ui.fastest_btn.clicked.connect(lambda: self.chosen_way(1))
        self.ui.shortest_btn.clicked.connect(lambda: self.chosen_way(2))

        self.scene = QGraphicsScene(0,0,1280,900)

        # directions = self.shortest_path(self.graph, 4, 1)

        self.ui.graphicsView.setScene(self.scene)
        now = datetime.now()
        current_time = now.strftime("%H")
        self.get_trafics(current_time)

       

        self.set_destination_style(self.nodes_destination_style,self.previous_end)
        self.reset_graph()
    
    def set_destination_style(self,style,previous):
        cnt = 1
        while cnt <= len(self.nodes_dict):
            if self.nodes_dict[cnt][1] != previous:
                self.nodes_dict[cnt][1].setStyleSheet(style)
        
            cnt +=1
    

    def shortest_path(self, graph, node1, node2):
        path_list = [[node1]]
        path_index = 0

        previous_nodes = {node1}

        if node1 == node2:
            return path_list[0]
        
        while path_index < len(path_list):
            current_path = path_list[path_index]
            last_node = current_path[-1]
            next_nodes = graph[last_node]

            if node2 in next_nodes:
                current_path.append(node2)
                return current_path
            
            for next_node in next_nodes:
                if not next_node in previous_nodes:
                    new_path = current_path[:]
                    new_path.append(next_node)
                    path_list.append(new_path)

                    previous_nodes.add(next_node)
            
            path_index += 1

        return []
    
    
    def eventFilter(self, widget, event):
        if widget == self.ui.depart_line:
            if event.type() == QEvent.FocusOut:
                pass
            elif event.type() == QEvent.FocusIn:
                self.clicked.emit()   # When the focus falls again, edit Enter the box, send clicked Signal out 
            else:
                pass
        
        elif widget == self.ui.depaarture_line:
            if event.type() == QEvent.FocusOut:
                pass
            elif event.type() == QEvent.FocusIn:
                self.destination_click.emit()
            else:
                pass

        return False

    def set_destination_true(self):
        self.set_destination_style(self.nodes_start_style, self.previous_end)
        self.destination = True
    
    def set_destination_false(self):
        self.set_destination_style(self.nodes_destination_style, self.previous_start)
        self.destination = False
    
    def reverse(self):
        if self.selected_destination:
            self.starting_point = self.selected_destination[3]
            self.ending_point = self.selected_start[3]
            new_revers = self.selected_destination
            self.ui.depaarture_line.setText(f"  {self.selected_start[2]}")
            self.ui.depart_line.setText(f"  {self.selected_destination[2]}")
            self.selected_destination[1].setStyleSheet(self.selected_start_style)
            self.selected_start[1].setStyleSheet(self.selected_destination_style)
            self.previous_start = self.selected_destination[1]
            self.previous_end = self.selected_start[1]
            self.selected_destination = self.selected_start
            self.selected_start = new_revers
            
    
    def find_path(self):
        self.chosen_way(self.choise)
        self.cnt = 0
        self.ui.filtered_label.hide()
        if self.starting_point != 0 and self.ending_point != 0:
            self.filter = True
            if str(self.ui.change_time_btn.text()) == "Şimdi ayrıl ▼":
                now = datetime.now()
                current_time = now.strftime("%H")
                self.get_trafics(current_time)
            
            else:
                self.get_trafics(self.ui.hours_combo.currentText())

            self.reset_graph()
            for i in self.scene.items():
                self.scene.removeItem(i)
            traffic_found = False
            cnt = 0
            directions = self.shortest_path(self.graph, self.starting_point, self.ending_point)
            self.speed = 40
            self.trafic_animation = self.draw_path(self.red, directions)
            self.ui.trafikli_distance.setText(f"{800 * len(directions)/1000} km")
            self.ui.trafikli_time.setText(f"{round((800 * len(directions)/1000/self.speed * 60), 3)} min")
            self.ui.trafikli_frame.show()

            # print(directions)
            while cnt < len(directions) -1:
                traffic = self.nodes_dict[directions[cnt + 1]][4] + self.nodes_dict[directions[cnt]][4]
                if abs(traffic) >= 60:
                    self.graph[directions[cnt]].remove(directions[cnt + 1])
                    self.graph[directions[cnt + 1]].remove(directions[cnt])
                    directions = self.shortest_path(self.graph, self.starting_point, self.ending_point)
                    self.speed = 90
                    # print(directions)
                    traffic_found = True          

                cnt +=1
            
            if traffic_found:
                self.trafic_animation = self.draw_path(self.blue, directions)
                self.ui.trafiksiz_distance.setText(f"{800 * len(directions)/1000} km")
                self.ui.trafiksiz_time.setText(f"{round((800 * len(directions)/1000/self.speed * 60), 3)} min")
                self.ui.trafiksiz_frame.show()
            else:
                self.filter = False
                self.trafiksiz_animation = self.trafic_animation = self.draw_path(self.blue, directions)
                self.ui.trafiksiz_distance.setText(f"{800 * len(directions)/1000} km")
                self.ui.trafiksiz_time.setText(f"{round((800 * len(directions)/1000/self.speed * 60), 3)} min")
                self.ui.trafiksiz_frame.show()
                self.ui.filtered_label.hide()
                self.ui.trafikli_frame.hide()
            
            self.ui.start_path_btn.show()
    
    def draw_path(self, color, directions):
        if len(directions) > 1:
            animation_list = []
            cnt = 0
            covered_distance = 0
            # print(directions)
            while cnt < len(directions)-1:
                pen = QPen(QBrush(color), 4)

                x1 = self.nodes_dict[directions[cnt]][0][0]
                x2 = self.nodes_dict[directions[cnt]][0][1]
                y1 = self.nodes_dict[directions[cnt + 1]][0][0]
                y2 = self.nodes_dict[directions[cnt + 1]][0][1]

                animation_list.append([x1, x2])

                current_distance = math.sqrt((x2-x1)**2 + (y2 - y1)**2)
                covered_distance += current_distance
                
                self.scene.addLine(x1, x2, y1, y2, pen)
                cnt+=1
            
            animation_list.append([y1,y2])
            
            return animation_list
        
    
    def reset_graph(self):
        self.graph[1] = {2,8,4}
        self.graph[2] = {1,11,3}
        self.graph[3] = {2,4,10}
        self.graph[4] = {3,1,5}
        self.graph[5] = {4,6,12}
        self.graph[6] = {5,7}
        self.graph[7] = {6,8}
        self.graph[8] = {7,1}
        self.graph[9] = {12,10}
        self.graph[10] = {9,3,11}
        self.graph[11] = {2,10}
        self.graph[12] = {9,5}
    
    def get_trafics(self, current_time):
        print(int(current_time))
        if 7 <= int(current_time) <= 12 or 16 <= int(current_time) <= 19:
            self.traffic_array = [0,0,40,40,0,0,0,0,40,40,40,0]
        
        elif 13 <= int(current_time) <= 15 or 20 <= int(current_time) <= 23:
            self.traffic_array = [0,0,0,0,0,0,0,0,40,40,40,0]
        
        elif 0 <= int(current_time) <= 6:
            self.traffic_array = [0,0,0,0,0,0,0,0,0,0,0,0]
        
        self.nodes_dict = {
            1: [self.node_1, self.ui.node_1, "Pamukkale ün. Mor. Yem",1,self.traffic_array[0]],
            2: [self.node_2, self.ui.node_2, "Pamukkale ün. Hospital",2,self.traffic_array[1]],
            3: [self.node_3, self.ui.node_3, "Pamukkale ün. İl. Fak",3,self.traffic_array[2]],
            4: [self.node_4, self.ui.node_4, "PAÜ Kınıklı",4,self.traffic_array[3]],
            5: [self.node_5, self.ui.node_5, "Hasan Kasapoğlu Kül. Mer.",5,self.traffic_array[4]],
            6: [self.node_6, self.ui.node_6, "Pamukkale ün. Tek. Fak",6,self.traffic_array[5]],
            7: [self.node_7, self.ui.node_7, "Pamukkale University",7,self.traffic_array[6]],
            8: [self.node_8, self.ui.node_8, "Pamukkale ün. İk. ve İd.",8,self.traffic_array[7]],
            9: [self.node_9, self.ui.node_9, "Zater Döner",9,self.traffic_array[8]],
            10: [self.node_10, self.ui.node_10, "Denizli Polis evi",10,self.traffic_array[9]],
            11: [self.node_11, self.ui.node_11, "Starbucks",11,self.traffic_array[10]],
            12: [self.node_12, self.ui.node_12, "Abnini DENIZLI",12,self.traffic_array[11]]
        }

    def chosen_way(self, choice):
        if self.filter:
            choose_list = [self.ui.trafikli_frame, self.ui.trafiksiz_frame]
            self.choose_time = [float(self.ui.trafikli_time.text().split()[0]), float(self.ui.trafiksiz_time.text().split()[0])]
            self.choose_way = [float(self.ui.trafikli_distance.text().split()[0]), float(self.ui.trafiksiz_distance.text().split()[0])]

            min_time_index = self.choose_time.index(min(self.choose_time))
            min_distance_index = self.choose_way.index(min(self.choose_way))
            
            if choice == 1:
                for i in choose_list:
                    i.hide()
                choose_list[min_time_index].show()
                # choose_list[min_time_index].move(1310, 460)
                self.ui.filtered_label.setText("En hızlı yol")
                self.ui.filtered_label.show()
            
            elif choice == 2:
                for i in choose_list:
                    i.hide()
                choose_list[min_distance_index].show()
                # choose_list[min_distance_index].move(1310, 460)
                self.ui.filtered_label.setText("En kısa yol")
                self.ui.filtered_label.show()
            
            else:
                for i in choose_list:
                    i.hide()
    
    def path_animation(self):
        if self.cnt < len(self.trafic_animation) - 1:
            self.ui.animation_frame.show()
            self.animation = QPropertyAnimation(self.ui.animation_frame, b"pos")
            self.animation.setDuration(1500)
            self.animation.setStartValue(QPoint(self.trafic_animation[self.cnt][0] - 24, self.trafic_animation[self.cnt][1] - 30))
            self.animation.setEndValue(QPoint(self.trafic_animation[self.cnt + self.add][0] - 24, self.trafic_animation[self.cnt + self.add][1] - 30))
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
            self.cnt += self.add
            # if self.cnt + 1 == len(self.trafic_animation):
            #     self.reverse()
            #     self.find_path()
            #     self.path_animation()
         
            self.animation.finished.connect(self.path_animation)
        
        else:
            self.reverse()

            if self.set_hours < 24:
                self.ui.hours_combo.setCurrentIndex(self.set_hours)
            
            else:
                self.set_hours = 0
                self.ui.hours_combo.setCurrentIndex(self.set_hours)
            self.set_hours += 1
            Ui_Functions.depart_now(self, f"{self.ui.hours_combo.currentText()} : {self.ui.min_combo.currentText()}")
            self.find_path()
            self.path_animation()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ui_windows()

    win.show()
    sys.exit(app.exec_())