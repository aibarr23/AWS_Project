

KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex


MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        md_bg_color: get_color_from_hex("#000a12")
        color_normal: get_color_from_hex("#718089")
        color_active: get_color_from_hex("#f3ab44")
        title: "Automated Watering APP"
        elevation: 10
        right_action_items: [["brightness-4", app.theme_style]]

    
    MDTabs:
        text_color_active: get_color_from_hex("#f3ab44")
        tab_hint_x: True
        id: tabs
        

        Weather_tab:
            id: weathertab
            icon: "weather-sunny"
            color_active: get_color_from_hex("#f3ab44")

            

            MDBoxLayout:
                orientation: "vertical"
                

                MDToolbar:
                    id: weatherheading
                    elevation: 10
                    halign: "center"

                    title: app.Current_City
                    pos_hint: {"center_y": .5, "pos_hint_x": 0.5}
                    font_style: "H4"

                    
                    right_action_items: [["refresh", app.refresh_weather, "Refresh"]]
                    
                    MDFlatButton:
                        pos_hint: {"center_y": .5, "pos_hint_x":0.5}
                        text: "auto-refresh->"
                        text_color: get_color_from_hex("#f3ab44")
                        padding: [0,0,0,0]
                    MDSwitch:
                        id: AR
                        on_press: app.refresh_weather('s')
                        pos_hint: {"center_y": .5, "pos_hint_x":0.5}
                        tooltip_text: "auto-refresh"
                
                MDStackLayout:
                    ScrollView:
                        id: scrview
                        pos_hint: {'center_x': .5}
                        adaptive_size: True
                        
                        MDList:
                            id: list
                            halign: "center"
                            cols: 1
                            rows: 5
                            spacing: "40dp"
                            
                            OneLineListItem:
                                id: datetime
                                text: app.getDT
                            
                                
                            MDCard:
                                orientation: "vertical"
                                size_hint: .5, None
                                height: "300dp"

                                padding: 30, 30, 30, 30
                                bg_light:
                                elevation: 20
                                radius: 40

                                MDLabel:
                                    halign: "center"
                                    font_style: "H5"
                                    text: "Weather for Today"

                                MDLabel:
                                    id: cd1line1
                                    halign: "center"
                                    font_style: "H1"
                                    text: app.CTemp

                                MDSeparator:

                                MDLabel:
                                    id: cd1line2
                                    halign: "center"
                                    font_style: "H4"
                                    text: app.Tdata
                                    

                            MDCard:
                                size_hint: .5, None
                                height: "300dp"

                                padding: 30, 30, 30, 30
                                bg_light:
                                elevation: 20
                                radius: 40


                                MDLabel:
                                    id: mdc2
                                    halign: "center"
                                    font_style: "H3"
                                    text: app.Wdata

                            MDCard:
                                size_hint: .5, None
                                height: "300dp"

                                padding: 30, 30, 30, 30
                                bg_light:
                                elevation: 20
                                radius: 40


                                MDLabel:
                                    id: mdc3
                                    halign: "center"
                                    font_style: "H4"
                                    text: app.Adata
            







        system_tab:
            icon: "wrench"

            MDBoxLayout:
                orientation: "vertical"
                # md_bg_color: get_color_from_hex("#344954")
                color_normal: get_color_from_hex("#718089")
                color_active: get_color_from_hex("#f3ab44")
            

                MDToolbar:
                    elevation: 10
                    halign: "center"

                    title: "System Status"
                    pos_hint: {"center_y": .5, "pos_hint_x": 0.5}
                    font_style: "H4"
                    right_action_items: [["reply-circle", app.Return_con, "Return Control"]]
                    
                    MDFlatButton:
                        pos_hint: {"center_y": .5, "pos_hint_x":0.5}
                        text: "Close All->"
                        text_color: get_color_from_hex("#f3ab44")
                        padding: [0,0,0,0]
                    MDIconButton:
                        id: CA
                        icon: "water-pump-off"
                        tooltip_text: "Close All"
                        on_press: app.close_sol('0')
                        pos_hint: {"center_y": .5, "pos_hint_x":0.5}

                MDStackLayout:
                    ScrollView:
                        pos_hint: {'center_x': .5}
                        adaptive_size: True
                        
                        
                        MDList:
                            halign: "center"
                            pos_hint: {'center_x': .5, 'center_y': .5}
                            cols: 2
                            rows: 5
                            spacing: "40dp"
                
                            MDLabel:
                                text: "Solenoid"
                                halign: "center"
                                font_style: "H4"
                                size_hint_y: None
                                height: self.texture_size[1]
                                pos_hint: {"center_y": .5}
                            MDLabel:
                                text: "Status"
                                halign: "center"
                                font_style: "H4"
                                size_hint_y: None
                                height: self.texture_size[1]
                                pos_hint: {"center_y": .5}
                            MDLabel:
                                text:"Solenoid #1"
                                halign: "center"
                                font_style: "H4"
                            MDSwitch:
                                id: S1
                                halign: "center"
                                on_press: app.close_sol('1')
                                disabled: True
                                pos_hint: {"center_y": .5, "pos_hint_x":0.5}
                            
                            MDLabel:
                                text: "Solenoid #2"
                                halign: "center"
                                font_style: "H4"
                            MDSwitch:
                                id: S2
                                on_press: app.close_sol('2')
                                disabled: True
                                pos_hint: {'center_x': .7, 'center_y': .5}
                            MDLabel:
                                text: "Solenoid #3"
                                halign: "center"
                                font_style: "H4"
                            MDSwitch:
                                id: S3
                                on_press: app.close_sol('3')
                                disabled: True
                                pos_hint: {"center_y": .5, "pos_hint_x":5}









        plant_tab:
            icon: "flower"

            MDBoxLayout:
                orientation: "vertical"
                # md_bg_color: get_color_from_hex("#344954")
                color_normal: get_color_from_hex("#718089")
                color_active: get_color_from_hex("#f3ab44")
            

                MDToolbar:
                    elevation: 10
                    halign: "center"

                    title: "Plant Information"
                    pos_hint: {"center_y": .5, "pos_hint_x": 0.5}
                    font_style: "H4"

                MDStackLayout:

                    ScrollView:
                        pos_hint: {'center_x': .5}
                        adaptive_size: True
                        
                        MDList:
                            halign: "center"
                            cols: 1
                            rows: 5
                            spacing: "40dp"

                            #start of first plant
                            MDCard:
                                orientation: "vertical"
                                size_hint: .5, None
                                height: "300dp"

                                padding: 30, 30, 30, 30
                                bg_light:
                                elevation: 20
                                radius: 40

                                MDLabel:
                                    halign: "center"
                                    font_style: "H3"
                                    text: "Plectranthus Venteri"

                                MDLabel:
                                    halign: "center"
                                    font_style: "H5"
                                    text: "Distinctive deeply lobed pelted leaves on self branching stout stems; the purplish mauve blossoms usually appear in late fall. Perfect where you need a tough as nails plant which gives an appearance of lacy delicacy"

                            
                            MDGridLayout:
                                cols: 1
                                row_default_height: (self.width - self.cols*self.spacing[0]) / self.cols
                                row_force_default: True
                                adaptive_height: True
                                padding: dp(4), dp(4)
                                spacing: dp(4)

                                SmartTileWithLabel:
                                    source: "plant1.jpg"
                                    text: "[size=26]Plectranthus Venteri in Experiment[/size]"
                                    allow_stretch: True
                                    keep_ratio: True

                            
                            MDCard:
                                orientation: "vertical"
                                size_hint: .5, None
                                height: "300dp"

                                padding: 30, 30, 30, 30
                                bg_light:
                                elevation: 20
                                radius: 40

                                MDLabel:
                                    id: M1
                                    halign: "center"
                                    font_style: "H5"
                                    text: app.moS1

                                MDLabel:
                                    halign: "center"
                                    font_style: "H5"
                                    text: "Plant #1 Watered by Solenoid --Solenoid number here-- "

                                MDSeparator:

                                MDLabel:
                                    id: M2
                                    halign: "center"
                                    font_style: "H5"
                                    text: app.moS2

                                MDLabel:
                                    halign: "center"
                                    font_style: "H5"
                                    text: "Plant #2 Watered by Solenoid --Solenoid number here-- "

                                MDSeparator:

                                MDLabel:
                                    id: M3
                                    halign: "center"
                                    font_style: "H5"
                                    text: app.moS3

                                MDLabel:
                                    halign: "center"
                                    font_style: "H5"
                                    text: "Plant #3 Watered by Solenoid --Solenoid number here-- "
                        
                        



'''

