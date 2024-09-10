from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def to_internal_value(self, data):

        # Avoid default error messages of ModelSerializer

        name = data.get('name', '').strip()
        if not name or name == "":
            raise serializers.ValidationError({"name": "Название не должно быть пустым."})

        price = data.get('price', None)
        if price in (None, '', 'null'):
            raise serializers.ValidationError({"price": "Не задана цена."})
        try:
            price = float(price)
        except ValueError:
            raise serializers.ValidationError({"price": "Цена должна быть числом."})
        if price <= 0:
            raise serializers.ValidationError({"price": "Цена должна быть положительным числом."})

        data['name'] = name
        data['price'] = price

        return super().to_internal_value(data)


