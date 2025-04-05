# Aplicación de Utilidades para Desarrolladores (Dev Utils App)

Una aplicación GUI en Python que proporciona varias funciones útiles para desarrolladores. Con una interfaz moderna y funciones convenientes, hace que el trabajo de desarrollo sea más eficiente.

![Captura de pantalla de la aplicación](screenshot.png)

## Características Principales

### Comparación de Texto (Text Diff)
- Muestra visualmente las diferencias entre dos textos
- Resaltado preciso de diferencias mediante comparación línea por línea
- Interfaz intuitiva para un uso sencillo
- Botón de reinicio para comenzar rápidamente un nuevo trabajo

### Visualizador de JSON
- Visualiza cadenas JSON como una estructura de árbol
- Funcionalidad de colapsar/expandir nodos para navegar fácilmente por estructuras complejas
- Datos de ejemplo proporcionados para pruebas rápidas
- Cambios automáticos de tema según el modo claro/oscuro

## Stack Tecnológico

- **Frontend**: CustomTkinter (biblioteca GUI de Python)
- **Algoritmo de Comparación**: biblioteca diff-match-patch
- **Análisis JSON**: módulo json integrado de Python
- **Sistema de Temas**: soporte para modo claro/oscuro

## Requisitos del Sistema

- Python 3.8 o superior
- Los siguientes paquetes de Python:
  - customtkinter
  - pillow
  - diff-match-patch

## Instalación

### 1. Clonar Repositorio
```bash
git clone https://github.com/ghdquddnr/dev_utils_app.git
cd dev_utils_app
```

### 2. Configurar Entorno Virtual e Instalar Paquetes
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Instalar paquetes
pip install customtkinter pillow diff-match-patch
```

### 3. Ejecutar Aplicación
```bash
python main.py
```

## Cómo Usar

### Función de Comparación de Texto
1. Ingrese el texto original en el área de texto izquierda.
2. Ingrese el texto a comparar en el área de texto derecha.
3. Haga clic en el botón "Comparar" para ver las diferencias entre los dos textos resaltadas con colores.
   - Partes eliminadas: Fondo rojo
   - Partes añadidas: Fondo verde
4. Haga clic en el botón "Reiniciar" para borrar todo el texto y comenzar una nueva comparación.

### Función de Visualizador de JSON
1. Ingrese una cadena JSON en el área de texto izquierda.
2. Haga clic en el botón "Convertir" para visualizar el JSON como una estructura de árbol a la derecha.
3. Haga clic en los botones + o - en los nodos del árbol para expandirlos o colapsarlos.
4. Use el botón "Expandir Todo"/"Colapsar Todo" para controlar todo el árbol a la vez.
5. Haga clic en el botón "Datos de Ejemplo" para ingresar automáticamente datos JSON de muestra.
6. Haga clic en el botón "Reiniciar" para borrar todos los datos.

### Cambio de Tema
- Haga clic en el botón "Cambiar Tema" en la parte inferior de la barra lateral para cambiar entre los modos claro y oscuro.

## Configuración del Entorno de Desarrollo

```bash
# Instalar paquetes de desarrollo
pip install -e ".[dev]"
```

## Planes Futuros

- Funciones de utilidad adicionales en desarrollo
- Optimización de rendimiento
- Funcionalidad de guardado de configuración de usuario

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Para más detalles, consulte el archivo [LICENSE](LICENSE).

## Contribución

¡Las contribuciones son siempre bienvenidas! Puede ayudar a mejorar este proyecto a través de informes de errores, solicitudes de funciones o contribuciones de código. 