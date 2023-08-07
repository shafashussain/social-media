from rest_framework.views import APIView
from django.core.paginator import Paginator

from social_media.models.post_model import PostModel
from social_media.models.user_model import UserModel
from social_media.models.admin_model import AdminModel
from social_network.responses.response_handling import ResponseHandling


class PostView(APIView):
    def get(self, request):
        """
        Used to list of posts
        """
        try:
            payload = request.data.dict()
            page = payload.pop("page", 1)

            posts = PostModel.objects.values_list()
            paginator = Paginator(posts, 10)    # One page contains 10 posts
            page_obj = paginator.get_page(page)
            pages = {
                "current_page_number": page_obj.number,
                "total_pages": paginator.num_pages
            }

            return ResponseHandling.retrieve_list_success(page_obj, pages)
        except Exception as e:
            return ResponseHandling.bad_request(str(e))
