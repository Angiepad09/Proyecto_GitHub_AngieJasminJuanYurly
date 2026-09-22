while True:

    try:
        print("------------------------------------")
        print("BIBLIOTECA HORIZONTE")   
        print("Bienvenido a BiblioStock")
        print("------------------------------------")
        print("Seleccione la opcion segun lo que deseas realizar:\n")
        opcion_menu=int(input(
            "1.Registrar item\n" \
            "2.Listar items\n" \
            "3.Buscar item\n" \
            "4.Registrar prestamo\n" \
            "5.Registrar devolucion\n" \
            "6.Salir\n "
        ))

        if opcion_menu == 6:
            print("Haz finalizado el programa, hasta pronto")
            break

        elif opcion_menu ==1:
            #registrar_item()
            pass

        elif opcion_menu ==2:
           pass
        

        elif opcion_menu ==3:
            pass    

        elif opcion_menu ==4:
            pass    

        elif opcion == "6":
            print("\nGracias por utilizar BiblioStock.")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")
    except ValueError:
        print("Ingrese una opcion del menu correcta")
       