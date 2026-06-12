from docxtpl import DocxTemplate
import uuid
from loguru import logger
import os


def fill_docx_template(template_name, template_path, context):
    """
    Функция для заполнения шаблона docx.

    Параметры:
    template_path (str): путь к пустому шаблону (например, 'template.docx').
    output_path (str): путь, куда сохранить готовый файл (например, 'ready_lawsuit.docx').
    context (dict): словарь с данными для заполнения (ключи - это метки в шаблоне).
    """
    real_path = os.path.join("templates", template_path)
    doc = DocxTemplate(real_path)

    doc.render(context)
    file_name = f"{template_name}_{uuid.uuid4()}.docx"
    doc.save(f"data/{file_name}")
    logger.success(f"Документ сохранен в файл: data/{file_name}")

    return file_name
