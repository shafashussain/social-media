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
    def query_success(message):
        """
        This method is called when a query is success.
        :return:
        """
        message = {
            'status': "success",
            'code': 200,
            'message': message,
        }
        return JsonResponse(message, status=200)

    # --------------------------------------------------------------

    @staticmethod
    def login_success(data=None):
        """
        This method is called when the login is successful.
        :return:
        """
        message = {
            'status': "success",
            'code': 200,
            'message': "Logged in successfully.",
            'data': data
        }
        return JsonResponse(message, status=200)

    # --------------------------------------------------------------

    @staticmethod
    def logout_success():
        """
        This method is called when the logout is successful.
        :return:
        """
        message = {
            'status': "success",
            'code': 200,
            'message': "Logged out successfully.",
        }
        return JsonResponse(message, status=200)

    # --------------------------------------------------------------

    @staticmethod
    def reference_error():
        """
        The method is called when the reference id is wrong or not exists.
        :return:
        """
        message = {
            'status': "error",
            'code': 404,
            'message': "Invalid reference id."
        }
        return JsonResponse(message, status=404)

    # --------------------------------------------------------------

    @staticmethod
    def input_format_error(suggestion=None):
        """
        The method is called when datatype is mismatched or some required data is missed.
        :return:
        """
        message = {
            'status': "error",
            'code': 422,
            'message': "Some required fields are either empty or incorrect.",
            'suggestion': suggestion
        }
        return JsonResponse(message, status=422)

    # --------------------------------------------------------------

    @staticmethod
    def retrieve_success(data=None):
        """
        The method is called when data fetched successfully.
        :param data:
        :return:
        """
        message = {
            'status': "success",
            'code': 200,
            'message': "Retrieved successfully.",
            'data': data,
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
    def retrieve_list_success_with_requested_data(data=None, pages=None, request_data=None):
        """
        This method is called to fetch list of data along with requested data.
        :param data:
        :param pages:
        :return:
        """
        message = {
            'status': "success",
            'code': 200,
            'message': "Retrieved successfully.",
            'data': data,
            'pages': pages,
            'cultivation_details': request_data,
        }
        return JsonResponse(message, status=200)

    # --------------------------------------------------------------

    @staticmethod
    def no_records(error_message="Records unavailable."):
        """
        The method is called when table haven't any record.
        :param data:
        :return:
        """
        message = {
            'status': "error",
            'code': 404,
            'message': error_message,
        }
        return JsonResponse(message, status=404)

    # --------------------------------------------------------------

    @staticmethod
    def update_success(data=None):
        """
        The method is called when record updated successfully.
        :param data:
        :return:
        """
        message = {
            'status': "success",
            'code': 200,
            'message': "updated successfully.",
            'data': data
        }
        return JsonResponse(message, status=200)

    # --------------------------------------------------------------

    @staticmethod
    def permission_denied(message=None):
        """
        The method is called when the user not have the permission to access.
        :return:
        """
        message = {
            'status': "error",
            'code': 403,
            'message': message
        }
        return JsonResponse(message, status=403)

    # --------------------------------------------------------------

    @staticmethod
    def record_not_found(message="Matching record doesn't exist"):
        """
        The method is called when records are not found.
        :param message:
        :return:
        """
        message = {
            'status': "error",
            'code': 404,
            'message': message
        }
        return JsonResponse(message, status=404)

    # --------------------------------------------------------------

    @staticmethod
    def delete_success():
        """
        The method is called when record deleted from database.
        :return:
        """
        message = {
            'status': "success",
            'code': 200,
            'message': "Record deleted successfully"
        }
        return JsonResponse(message, status=200)

    # --------------------------------------------------------------

    @staticmethod
    def authentication_failed(message=None):
        message = {
            'status': "error",
            'code': 401,
            'message': message
        }
        return JsonResponse(message, status=401)

    # --------------------------------------------------------------

    @staticmethod
    def duplicate_entry(message="Data already exists."):
        message = {
            'status': "error",
            'code': 409,
            'message': message
        }
        return JsonResponse(message, status=409)

    # --------------------------------------------------------------

    @staticmethod
    def mobile_number_eligible():
        message = {
            'status': "success",
            'code': 200,
            'message': "Mobile number is eligible for registration."
        }
        return JsonResponse(message, status=200)

    # --------------------------------------------------------------

    @staticmethod
    def mobile_number_already_exists():
        message = {
            'status': "error",
            'code': 409,
            'message': "Mobile number is already registered."
        }
        return JsonResponse(message, status=409)

    # --------------------------------------------------------------

    @staticmethod
    def internal_server_error():
        message = {
            'status': "error",
            'code': 500,
            'message': "Request failed due to internal server error"
        }
        return JsonResponse(message, status=500)

    # --------------------------------------------------------------

    @staticmethod
    def cannot_delete_record(message):
        """
        The method is called when record is linked to other data and cannot perform delete
        :return:
        """
        message = {
            'status': "error",
            'code': 409,
            'message': message
        }
        return JsonResponse(message, status=409)

    # --------------------------------------------------------------

    @staticmethod
    def employee_does_not_exists():
        """
        The method is called when the employee ID does not exists.
        :return:
        """
        message = {
            'status': "error",
            'code': 404,
            'message': "Employee does not exists."
        }
        return JsonResponse(message, status=404)

    # --------------------------------------------------------------

    @staticmethod
    def cannot_update_record(message):
        """
        The method is called when record is linked to other data and cannot perform update
        :return:
        """
        message = {
            'status': "error",
            'code': 409,
            'message': message
        }
        return JsonResponse(message, status=409)

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
