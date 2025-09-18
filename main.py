import typer

app = typer.Typer()

@app.command()
def main():
    while True:
        print("\n*------Sistema de asistencia------*\n")
        print("1. Marcar asistencia")
        print("2. Marcar salida")
        print("3. Generar reporte")
        print("4. Salir")

        opcion = typer.prompt("\nIngrese una opción: ", type=int)

        match opcion:
            case 1:
                print("\nMarcar asistencia\n")
            case 2:
                print("\nMarcar salida\n")
            case 3:
                print("\nGenerar reporte\n")
            case 4:
                print("\nSalir\n")
                False
                break
            case _:
                print("\nOpción inválida\n")

if __name__ == "__main__":
    app()