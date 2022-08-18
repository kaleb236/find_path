 ##########BUTTONS ########
        # self.ui.node_1.clicked.connect(lambda: self.show_starting(1))
        # self.ui.node_2.clicked.connect(lambda: self.show_starting(2))
        # self.ui.node_3.clicked.connect(lambda: self.show_starting(3))
        # self.ui.node_4.clicked.connect(lambda: self.show_starting(4))
        # self.ui.node_5.clicked.connect(lambda: self.show_starting(5))
        # self.ui.node_6.clicked.connect(lambda: self.show_starting(6))

        # #########SELECTING############
        # self.ui.start_point.clicked.connect(self.select_start)
        # self.ui.end_point.clicked.connect(self.select_end)
        # self.ui.start_btn.clicked.connect(self.start_path)


# def select_start(self):
    #     for i in range(1, 7):
    #         if i == self.previous_start:
    #             continue
    #         self.nodes_ui_dict[i].setText("")
    #     self.nodes_ui_dict[self.selected].setStyleSheet("""
    #     color: rgb(85, 170, 0);
    #     font: 63 16pt "Bahnschrift SemiBold";
    #     """)
    #     self.nodes_ui_dict[self.selected].setText("Ba")
    #     self.previous_end = self.selected
    #     self.starting = self.selected
    #     self.ui.start_frame.hide()
    
    # def select_end(self):
    #     for i in range(1, 7):
    #         if i == self.previous_end:
    #             continue
    #         self.nodes_ui_dict[i].setText("")
    #     self.nodes_ui_dict[self.selected].setStyleSheet("""
    #     color: rgb(255, 0, 0);
    #     font: 63 14pt "Bahnschrift SemiBold";
    #     """)
    #     self.nodes_ui_dict[self.selected].setText("Bi")
    #     self.previous_start = self.selected
    #     self.ending = self.selected
    #     self.ui.start_frame.hide()
    
    # def show_starting(self, x):
    #     self.selected = x
    #     self.ui.start_frame.move(self.nodes_dict[x][0], self.nodes_dict[x][1])
    #     self.ui.start_frame.show()
    
    # def start_path(self):
    #     self.draw(self.shortest_path(self.graph, self.starting, self.ending))
    
    # def draw(self, directions):
    #     cnt = 0
    #     while cnt < len(directions)-1:
    #         pen = QPen(QBrush(QColor(200,0,0,255)), 4)
    #         self.scene.addLine(self.nodes_dict[directions[cnt]][0],self.nodes_dict[directions[cnt]][1],self.nodes_dict[directions[cnt+1]][0],self.nodes_dict[directions[cnt+1]][1], pen)
    #         cnt+=1
        
    #     cnt = 0
    #     if 2 in directions:
    #         self.graph[2] = {1}
    #         self.graph[3] = {4}
    #         directions_2 = self.shortest_path(self.graph, self.starting, self.ending)
        
    #         while cnt < len(directions_2)-1:
    #             pen = QPen(QBrush(QColor(0,0,200,255)), 4)
    #             self.scene.addLine(self.nodes_dict[directions_2[cnt]][0],self.nodes_dict[directions_2[cnt]][1],self.nodes_dict[directions_2[cnt+1]][0],self.nodes_dict[directions_2[cnt+1]][1], pen)
    #             cnt+=1
        
    #     else:
    #         cnt = 0
    #         while cnt < len(directions)-1:
    #             pen = QPen(QBrush(QColor(0,0,200,255)), 4)
    #             self.scene.addLine(self.nodes_dict[directions[cnt]][0],self.nodes_dict[directions[cnt]][1],self.nodes_dict[directions[cnt+1]][0],self.nodes_dict[directions[cnt+1]][1], pen)
    #             cnt+=1
        
    #     cnt = 0