import dropbox 

class TransferData:

    def __init__(self,acessToken):
      self.acessToken=acessToken

    def uploadFiles(self,source,destination):
        upload=dropbox.Dropbox(self.acessToken)

        file=open(source,'rb')
        upload.files_upload(file.read(),destination)

def main():
    accessToken='sl.A44rV96Gk5wuOgy-u3m1neQV0mDCAec0nzh_puTVahWIt0fJPh_whO3TfVq08Ye-_NcOrvzz4WpKQRZESjXgJFO33UuzcrBQ6cUADzb9qWzt14-BdGSrK6GmKAwnTGSawxSA2IA'
    object=TransferData(accessToken)
    source=input('Enter File Which You Want To Transfer : ')
    destination=input('Enter the Destination Where You Want To Move : ')
    object.uploadFiles(source,destination)
    print('Your Files Has Been Transfered')


main()

