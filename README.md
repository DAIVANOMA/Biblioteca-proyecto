DANIEL ,  OMAR , IVAN , OBED , VICTOR  

# 📚 Biblioteca Digital con Open Library API
├── config.py
├── requirements.txt
├── README.md
├── models/
│   ├── __init__.py
│   └── book.py
├── services/
│   ├── __init__.py
│   ├── api_client.py
│   └── library_service.py
├── utils/
│   ├── __init__.py
│   └── cache.py
└── data/
    └── library.json
```

## ⚙️ Instalación

```bash
git clone https://github.com/tuusuario/biblioteca_api.git
cd biblioteca_api
pip install -r requirements.txt
```

## ▶️ Uso

```bash
python main.py
```

## 🧪 Ejemplo de salida

```text
Categoría: Programming
  - Clean Code | Robert C. Martin (2008)
  - The Pragmatic Programmer | Andrew Hunt (1999)
```

## 🔌 API utilizada

Este proyecto utiliza la API pública de Open Library:
https://openlibrary.org/developers/api

## 📈 Futuras mejoras

- Interfaz gráfica con Tkinter o PyQt.
- API REST con Flask o FastAPI.
- Base de datos con SQLite o PostgreSQL.
- Sistema de usuarios y favoritos.
- Exportación a PDF, CSV y Excel.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Puedes abrir un issue o enviar un pull request.

## 📄 Licencia

Este proyecto está bajo la licencia MIT.

## 👨‍💻 Autor

Daniel García
