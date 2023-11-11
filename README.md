# Proyecto-Cloud : predicción de precios de acciones

Este proyecto consiste en la implementación de un modelo de _machine learning_ para predecir los precios de las acciones de grandes empresas en _kubernetes_.

## Arquitectura

El proyecto consta de los siguientes componentes:

* **Modelo de machine learning:** El modelo de _machine learning_ está entrenado en un conjunto de datos históricos de precios de acciones. El modelo utiliza una red neuronal artificial para predecir los precios de las acciones de tipo LSTM.
* **Servidor web:** El servidor web proporciona una interfaz para que los usuarios interactúen con el modelo. El servidor web está implementado en _Python_ utilizando la biblioteca _Flask_.
* **Cluster de Kubernetes:** El cluster de _Kubernetes_ se utiliza para ejecutar el modelo y el servidor web.

## Explicación

El modelo de machine learning utilizado en este proyecto es una red neuronal artificial LSTM. La red neuronal se entrena en un conjunto de datos históricos de precios de acciones mediante una API de _Yahoo Finance_. El conjunto de datos consta de datos de precios de acciones de grandes empresas, como Apple, Microsoft, Amazon, entre otras.

El servidor web proporciona una interfaz para que los usuarios interactúen con el modelo. El servidor web utiliza la biblioteca _Flask_ para crear una aplicación web simple.

El cluster de _Kubernetes_ se utiliza para ejecutar el modelo y el servidor web. _Kubernetes_ es un sistema de orquestación de contenedores que facilita la ejecución de aplicaciones en la nube.

## Flujo

Para realizar una predicción, los pasos son los siguientes:

1. En el campo _"Month"_ y _"Day"_, ingresar la fecha deseada a predecir el precio de las acciones de la empresa Apple.
2. Hacer clic en el botón _“Predict”_. Tomará unos segundos en lo que se realiza el proceso de forecast para predecir los datos desde la fecha actual a la ingresada.
3. La página web mostrará la predicción del precio de las acciones de Apple para la fecha ingresada mediante un gráfico de líneas.

## Siguientes pasos
* Optimización del modelo de _machine learning_.
* Mejora de la interfaz del servidor web.
* Deployment de la aplicación.
* Opciones de distintas empresas para predecir los precios de las acciones.


