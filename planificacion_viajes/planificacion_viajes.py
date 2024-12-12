import reflex as rx

def index() -> rx.Component:
    return rx.container(
        #boton para cambiar el tema
        rx.color_mode.button(position="top-right"),
        
        rx.heading("PLANIFICA TU VIAJE!", size="9",color="white"),
        rx.hstack(
            rx.vstack(
                rx.text(
                "¡Ahorra tu tiempo para viajar.",
                size="5", color="white"
            ),
            rx.hstack(
                    rx.link(
                        rx.button("Registrate aqui!",background="white",color="black"),
                        href="https://docs.google.com/forms/d/e/1FAIpQLSf-b4fPqkBk_nQiErA-yZqtBbAmD1aMWO14VJ__FSgT8KlLbg/viewform?usp=dialog",
                        is_external=True,
                    ),
                    
                    rx.link(
                        rx.button(rx.icon(tag="instagram"),background="white",color="black"),
                        href="https://instagram.com",
                        is_external=True,
                    ),
                    rx.link(
                        rx.button(rx.icon(tag="facebook"),background="white",color="black"),
                        href="",
                        is_external=True,
                    ),
                    
                ),
                rx.image(src="avion.jpg"),
            ),
        
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.vstack(
             rx.text(
                "PAISES",
                size="5", color="white"
            ),
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("CHINA", value="tab1",color="white"),
                    rx.tabs.trigger("PERU", value="tab2",color="white"),
                    rx.tabs.trigger("PARIS", value="tab3",color="white"),
                    rx.tabs.trigger("BOLIVIA", value="tab4",color="white"),
                ),
                rx.tabs.content(
                    rx.image(src="6345c5fa3cd10.webp"),
                    rx.image(src="2021830-1630308695907.jpg"),
                    value="tab1",
                ),
                rx.tabs.content(
                    rx.image(src="istockphoto-479900992-612x612.jpg"),
                    rx.image(src="istockphoto-1387126975-612x612.jpg"),
                    value="tab2",
                ),
                rx.tabs.content(
                    rx.image(src="maxresdefault.jpg"),
                    rx.image(src="unnamed.jpg"),
                    value="tab3",
                ),
                rx.tabs.content(
                    rx.image(src="boliviahop-night.jpg"),
                    rx.image(src="bolivia-turismo.webp"),
                    value="tab4",
                ),
            ),
            
            margin_top="-270px"
        ), 
        bg="black"
    ),


app = rx.App()
app.add_page(index)