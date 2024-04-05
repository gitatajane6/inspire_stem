import flet as ft

def main(page:ft.Page):
    page.title="Learning FLET"
    content =ft.Column(
        controls=[
            ft.Text("This is a sample flet application",size=32,weight=600),
            ft.Row(
                spacing =20,
                controls=[
                    ft.Text("This is a row in flet")
                    ft.ElevatedButton("Click Me")
                    
                    ]
                
            )
        ft.Text("Welcome to learnig flet",size=16,weight)
        ],
        
     )

    #Dispaly our screen
    page.add()

ft.app(target=main)   