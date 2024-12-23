from rest_framework.decorators import api_view, permission_classes # for the api_view decorators (eg: @api_view(['GET']))
from rest_framework import status
from rest_framework.response import Response # for the response class
from .models import Match
from .serializers import MatchSerializer
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

# for Match table
class MatchTableViewSet:

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def createMatchEntry(request):
        serializer = MatchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    ########################

    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def getAllMatchEntries(request): # todo: add filtering
        user_id = request.GET.get('user_id')
        winner = request.GET.get('winner')
        loser = request.GET.get('loser')
        query = Q()
        if user_id:
            query |= Q(winner=user_id) | Q(loser=user_id)
        if winner:
            query &= Q(winner=winner)
        if loser:
            query &= Q(loser=loser)
        
        matchs = Match.objects.filter(query)
        serializer = MatchSerializer(instance=matchs, many=True)
        return Response(serializer.data)

    ########################

    @api_view(['DELETE'])
    @permission_classes([IsAuthenticated])
    def deleteMatchEntry(request):
        match_id = request.GET.get('match_id')
        if not match_id:
            return Response({"error": "the match id is not found."}, status=status.HTTP_404_NOT_FOUND)
        match = Match.objects.filter(match_id=match_id)
        match.delete()
        return Response(status=200, data={"success": "the match has been successfully deleted."})
    
