from rest_framework.views import APIView

from social_media.models.post_model import PostModel
from social_media.models.user_model import UserModel
from social_media.models.admin_model import AdminModel
from social_network.responses.response_handling import ResponseHandling


class PostLikeView(APIView):

    def post(self, request):
        """
        Used to add like to a post
        """
        try:
            payload = request.data.dict()
            post = PostModel.objects.get(primary_key=payload["post_id"])
            user = UserModel.objects.get(primary_key=payload["user_id"])

            is_dislike = False

            for dislike in post.dislikes.all():
                if dislike == user:
                    is_dislike = True
                    break

            if is_dislike:
                post.dislikes.remove(user)

            is_like = False

            for like in post.likes.all():
                if like == user:
                    is_like = True
                    break

            if not is_like:
                post.likes.add(user)
                # notification = Notification.objects.create(notification_type=1, from_user=user, to_user=post.author, post=post)

            # If want to perform remove like when an already liked post is liked Uncomment this
            # if is_like:
            #     post.likes.remove(user)

            return ResponseHandling.create_success(post)
        except Exception as e:
            return ResponseHandling.bad_request(str(e))


class PostDisLikeView(APIView):

    def post(self, request):
        """
        Used to add dislike to a post
        """
        try:
            payload = request.data.dict()
            post = PostModel.objects.get(primary_key=payload["post_id"])
            user = UserModel.objects.get(primary_key=payload["user_id"])

            is_like = False

            for like in post.likes.all():
                if like == user:
                    is_like = True
                    break

            if is_like:
                post.likes.remove(user)

            is_dislike = False

            for dislike in post.dislikes.all():
                if dislike == user:
                    is_dislike = True
                    break

            if not is_dislike:
                post.dislikes.add(user)

            # If want to perform remove dislike when an already liked post is liked Uncomment this
            # if is_dislike:
            #     post.dislikes.remove(user)

            return ResponseHandling.create_success(post)
        except Exception as e:
            return ResponseHandling.bad_request(str(e))


class PostDetailCountView(APIView):

    def get(self, request):
        """
        Used to add dislike to a post
        """
        try:
            payload = request.data.dict()
            # Only Admin will able to view the number of like/disliked of a post
            AdminModel.objects.get(primary_key=payload["admin_id"])

            post = PostModel.objects.get(primary_key=payload["post_id"])
            no_of_likes = post.total_likes()
            no_of_dislikes = post.total_dislikes()

            return ResponseHandling.success({
                "post_id": post.primary_key,
                "no_of_likes": no_of_likes,
                "no_of_dislikes": no_of_dislikes,
            })
        except Exception as e:
            return ResponseHandling.bad_request(str(e))


class PostLikedUsersView(APIView):

    def get(self, request):
        """
        Used to add dislike to a post
        """
        try:
            payload = request.data.dict()

            post = PostModel.objects.get(primary_key=payload["post_id"])
            liked_users = post.likes
            disliked_users = post.dislikes

            return ResponseHandling.success({
                "post_id": post.primary_key,
                "liked_users": liked_users,
                "disliked_users": disliked_users,
            })
        except Exception as e:
            return ResponseHandling.bad_request(str(e))
