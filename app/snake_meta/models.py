from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    imagen = models.CharField(max_length=200, null=True)
    correo = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    contraseña = models.CharField(max_length=100)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    fecha_n = models.CharField(max_length=45)
    rol = models.CharField(max_length=45)
    edad = models.IntegerField()
    Descripcion = models.CharField(max_length=300, null=True)
    imagen_fonodo = models.CharField(max_length=300, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'usuario'

class Serpiente(models.Model):
    idSerpiente = models.AutoField(primary_key=True)
    nombre3 = models.CharField(max_length=45)
    nombreCientifico = models.CharField(max_length=100)
    reino = models.CharField(max_length=45)
    especie = models.CharField(max_length=45)
    clase = models.CharField(max_length=45)
    genero = models.CharField(max_length=45)
    familia = models.CharField(max_length=45)
    imagen = models.CharField(max_length=200, null=True)
    venenosa = models.BooleanField()
    descripcion = models.CharField(max_length=2000)

    def __str__(self):
        return self.nombre3

    class Meta:
        db_table = 'serpiente'

class Georeferencia(models.Model):
    idGeoreferencia = models.AutoField(primary_key=True)
    fecha = models.CharField(max_length=20)
    zona = models.CharField(max_length=100)
    coordenadas = models.CharField(max_length=200)
    serpientes_id_serpientes = models.ForeignKey(
        Serpiente,
        on_delete=models.CASCADE,
        db_column='serpientes_id_serpientes'
    )
    usuario_id_usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column='usuario_id_usuario'
    )

    class Meta:
        db_table = 'georeferencia'

class TimestampMixin(models.Model):
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

class Reporte(TimestampMixin):
    idReporte = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000, null=True)
    imagen = models.CharField(max_length=200)
    serpientes_id_serpientes = models.ForeignKey(
        Serpiente,
        on_delete=models.CASCADE,
        null=True,
        db_column='serpientes_id_serpientes'
    )
    usuario_id_usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column='usuario_id_usuario'
    )

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'reporte'

class Comentario(TimestampMixin):
    idComentario = models.AutoField(primary_key=True)
    contenido = models.CharField(max_length=1000)
    reporte_id_reporte = models.ForeignKey(
        Reporte,
        on_delete=models.CASCADE,
        db_column='reporte_id_reporte'
    )
    usuario_id_usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column='usuario_id_usuario'
    )

    def __str__(self):
        return {
            'fecha de creacion': self.created_at,
            'contenido': self.contenido
        }

    class Meta:
        db_table = 'comentario'
        
