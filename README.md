# Proyecto-Cloud : predicción de precios de acciones

Este proyecto consiste en la implementación de un modelo de _machine learning_ para predecir los precios de las acciones de grandes empresas en _kubernetes_.

## Arquitectura

El proyecto consta de los siguientes componentes:

* **Modelo de machine learning:** El modelo de _machine learning_ está entrenado en un conjunto de datos históricos de precios de acciones. El modelo utiliza una red neuronal artificial para predecir los precios de las acciones de tipo LSTM.
* **Servidor web:** El servidor web proporciona una interfaz para que los usuarios interactúen con el modelo. El servidor web está implementado en _Python_ utilizando la biblioteca _Flask_ y _Gunicorn_. El uso de _Gunicorn_ con _Flask_ proporciona una solución sólida y escalable para implementar aplicaciones _Flask_ en producción. Mejora el rendimiento y admite el manejo de solicitudes simultáneas.
* **Cluster de Kubernetes:** El cluster de _Kubernetes_ se utiliza para ejecutar el modelo y el servidor web.

## Explicación

El modelo de machine learning utilizado en este proyecto es una red neuronal artificial LSTM. La red neuronal se entrena en un conjunto de datos históricos de precios de acciones mediante una API de _Yahoo Finance_. El conjunto de datos consta de datos de precios de acciones de grandes empresas, como Apple, Microsoft, Amazon, entre otras.

El servidor web proporciona una interfaz para que los usuarios interactúen con el modelo. El servidor web utiliza la biblioteca _Flask_ para crear una aplicación web simple.

El cluster de _Kubernetes_ se utiliza para ejecutar el modelo y el servidor web. _Kubernetes_ es un sistema de orquestación de contenedores que facilita la ejecución de aplicaciones en la nube.

## Flujo

Para realizar una predicción, los pasos son los siguientes:

1. Elegir una de las empresas disponibles en el menú dropdown de ‘Elegir una empresa’. En caso no encuentrat la empresa que se desea, escribir el nombre en el campo de ‘Agregar una empresa’.
2. En el campo _"Month"_ y _"Day"_, ingresar la fecha deseada a predecir el precio de las acciones de la empresa Apple.
3. Hacer clic en el botón _“Predict”_. Tomará unos segundos en lo que se realiza el proceso de forecast para predecir los datos desde la fecha actual a la ingresada.
4. La página web mostrará la predicción del precio de las acciones de la empresa seleccionada/ingresada para la fecha mediante un gráfico de líneas.
## Dificultades
* Debido al modelo empleado y la forma en que se predicen los datos, el modelo no se guarda y se reentrena cada vez que se realiza una consulta, lo cual dificulta la velocidad de obtención del valor del stock.
* Al momento de efectuar el deployment logra funcionar de manera local, pero nos genera errores al realizarlo en la nube, a pesar de contar con una instancia de tipo _large_. Luego se intentó probar con otra imagen, que logra ejecutarse sin problemas. 
