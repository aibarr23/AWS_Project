

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
        # right_action_items: [["menu", lambda x: app.callback_1()]]

    
    MDTabs:
        text_color_active: get_color_from_hex("#f3ab44")
        tab_hint_x: True
        id: tabs
        
        # md_bg_color: get_color_from_hex("#b9f6ca")
        # on_tab_switch: app.on_tab_switch(*args)
        
    # MDBottomAppBar:
    #     MDToolbar:
    #         title: "bottom"
    #         icon: "cog"
    #         left_action_items: [["coffee",lambda x: app.navigation()]]
    #         mode:'free-end'
    #         type:'bottom'
    

<Tab>
    MDBoxLayout:
        orientation: "vertical"
        # md_bg_color: get_color_from_hex("#344954")
        color_normal: get_color_from_hex("#718089")
        color_active: get_color_from_hex("#f3ab44")
       

        MDLabel:
            id: label
            text: "system"
            halign: "center"

        MDBoxLayout:
            orientation: "vertical"
            adaptive_height: True
            spacing: "12dp"

            MDIconButton:
                icon: "weather-sunny"
                user_font_size: "56sp"

            MDLabel:
                text: "MDLabel"
                font_style: "H5"
                size_hint_y: None
                height: self.texture_size[1]
                pos_hint: {"center_y": .5}



<plant_tab>
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






<system_tab>

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

        MDStackLayout:               

            ScrollView: 
                pos_hint: {'center_x': .5}
                adaptive_size: True
                
                MDList:
                    halign: "center"
                    cols: 1
                    rows: 5
                    spacing: "40dp"

        

                    MDLabel:
                        text: "Solenoid Status"
                        halign: "center"
                        font_style: "H4"
                        size_hint_y: None
                        height: self.texture_size[1]
                        pos_hint: {"center_y": .5}
                    MDSeparator:



<Weather_tab>
    icon: ""
    color_active: get_color_from_hex("#f3ab44")

    MDBoxLayout:
        orientation: "vertical"
        
        MDToolbar: 
            elevation: 10
            halign: "center"

            title: app.Current_City   
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
                            halign: "center"
                            font_style: "H1"
                            text: app.CTemp

                        MDSeparator:

                        MDLabel:
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
                            halign: "center"
                            font_style: "H3"
                            text: app.Pdata

                    MDCard:
                        size_hint: .5, None
                        height: "300dp"

                        padding: 30, 30, 30, 30
                        bg_light:
                        elevation: 20
                        radius: 40


                        MDLabel:
                            halign: "center"
                            font_style: "H4"
                            text: app.Adata
                    
                   


                        
                        


            
            
                

'''

