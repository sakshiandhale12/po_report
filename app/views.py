# myapp/views.py
from ninja import Router
from django.template import loader
from django.db import connections
from django.http import HttpResponse
import pdfkit

router = Router()

@router.get("/purchase_order/")
def purchase_order_view(request):
    # Fetch data from the database using raw SQL query
    with connections['eppsproud'].cursor() as cursor:
        cursor.execute("SELECT company_name, description_of_goods FROM purchase_order")
        purchase_orders = cursor.fetchall()

    # Render the HTML content from the template
    context = {'purchase_orders': purchase_orders}
    html_content = loader.render_to_string('po.html', context)

    # Specify the path for the output PDF file
    pdf_output_path = 'file.pdf'

    # Use pdfkit.from_string to convert HTML content to PDF
    pdfkit.from_string(html_content, pdf_output_path)

    # Serve the PDF as a response
    with open(pdf_output_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'filename=file.pdf'
        return response
# from django.http import HttpResponse
# import pdfkit
# from django.shortcuts import render

# def generate_pdf(request):
#     # Sample data for purchase orders (replace this with your actual data)
#     purchase_orders = [
#         {
#             'company_name': '',
#             'address': '123 Main St',
#             'registered_address': '456 Regd St',
#             'contact_number': '555-1234',
#             'email': 'companya@example.com',
#         },
#         # Add more purchase orders as needed
#     ]

#     context = {
#         'purchase_orders': purchase_orders,
#     }

#     # Render the HTML template with the context
#     html_content = render(request, 'po.html', context).content.decode('utf-8')

#     # Create a PDF file in memory
#     pdf_file = pdfkit.from_string(html_content, False)

#     # Set response headers for PDF download
#     response = HttpResponse(pdf_file, content_type='application/pdf')
#     response['Content-Disposition'] = 'filename="output.pdf"'

#     return response



