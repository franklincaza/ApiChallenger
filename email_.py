import win32com.client as win32

def enviarEmail(remitente,body,asunto):
    # Crear una instancia de Outlook
    outlook = win32.Dispatch('Outlook.Application')
    namespace = outlook.GetNamespace("MAPI")

    # Crear un nuevo mensaje
    correo = outlook.CreateItem(0)

    # Configurar el destinatario, asunto y cuerpo del mensaje
    correo.Subject = asunto
    correo.To = remitente
    correo.HTMLBody = body

    # Adjuntar archivos si es necesario
    # correo.Attachments.Add('ruta_del_archivo')

    # Enviar el correo
    correo.Send()

    print("El correo electrónico ha sido enviado correctamente.")
