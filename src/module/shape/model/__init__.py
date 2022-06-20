from src.postgres import pg_handler
from src.module.shape.model.shape import Shape
from src.module.shape.model.rectangle import Rectangle


Rectangle = Rectangle
Shape.metadata.create_all(pg_handler.get_engine())
