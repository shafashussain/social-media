from django.http import JsonResponse


class ResponseHandling:

    def __init__(self):
        pass

    # --------------------------------------------------------------

    @staticmethod
    def create_success(data=None):
        """
        The method called when a new record is created successfully.
        :param data:
        :return:
        """
        message = {
            'status': "success",
            'code': 201,
            'message': "Created successfully.",
            'data': data
        }
        return JsonResponse(message, status=201)

    # --------------------------------------------------------------

    @staticmethod
    def success():
        """
        This method is called when a query is executed successfully.
        :return:
        """
        message = {
            'status': "success",
            'code': 200,
            'message': "Success.",
        }
        return JsonResponse(message, status=200)

    # --------------------------------------------------------------

    @staticmethod
    def retrieve_list_success(data=None, pages=None):
        """
        This method is called to fetch list of data.
        :param data:
        :param pages:
        :return:
        """
        message = {
            'status': "success",
            'code': 200,
            'message': "Retrieved successfully.",
            'data': data,
            'pages': pages
        }
        return JsonResponse(message, status=200)

    # --------------------------------------------------------------

    @staticmethod
    def bad_request(message):
        """
        The method is called when the request could not be performed
        :return:
        """
        message = {
            'status': "error",
            'code': 400,
            'message': message
        }
        return JsonResponse(message, status=400)
