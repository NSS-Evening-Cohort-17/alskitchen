""" A module for handling Menu Items requests """
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from alskitchenapi.models import MenuItem


class MenuItemView(ViewSet):
    """ Menu Items Viewset """
    
    def retrieve(self, request, pk):
        """ Handle a GET request for a menu item """
        try:
            menu_item = MenuItem.objects.get(pk=pk)
            serializer = MenuItemSerializer(menu_item)
            return Response(serializer.data)
        except MenuItem.DoesNotExist as e:
            return Response({"Duley what was your Q"}, status=status.HTTP_404_NOT_FOUND)
        
    
    def list(self, request):
        """ Handle a GET request for all of the menu items """
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)

class MenuItemSerializer(serializers.ModelSerializer):
    """ JSON serializer for menu items """
    class Meta:
        model = MenuItem
        fields = (
            'id',
            'title',
            'description',
            'type',
            'wine_pairing')