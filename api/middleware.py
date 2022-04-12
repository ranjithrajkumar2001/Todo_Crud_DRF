class TrackResponse_Middleware:
    def __init__(self,get_respone):
        self.get_respone=get_respone

    def __call__(self,request):
        response = self.get_respone(request)
        print("Source of Request : ",request.META['HTTP_USER_AGENT'])
        return response