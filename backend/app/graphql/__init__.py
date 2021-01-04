import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import User as UserModel, Cart as CartModel, Product as ProductModel, Seller as SellerModel
from sqlalchemy.orm import class_mapper

class_mapper(UserModel)
class_mapper(CartModel)
class_mapper(ProductModel)
class_mapper(SellerModel)


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        only_fields = ("email",)


class Cart(SQLAlchemyObjectType):
    class Meta:
        model = CartModel
        exclude_fields = ("created_at", "updated_at")


class Product(SQLAlchemyObjectType):
    class Meta:
        model = ProductModel
        exclude_fields = ("created_at", "updated_at")


class Seller(SQLAlchemyObjectType):
    class Meta:
        model = SellerModel
        exclude_fields = ("created_at", "updated_at")


class Query(graphene.ObjectType):
    users = graphene.List(User)
    sellers = graphene.List(Seller)
    cart = graphene.List(Cart)
    products = graphene.List(Product)

    def resolve_users(self, info):
        query = User.get_query(info)
        return query.all()

    def resolve_sellers(self, info):
        query = Seller.get_query(info)
        return query.all()

    def resolve_cart(self, info):
        query = Cart.get_query(info)
        return query.all()

    def resolve_product(self, info):
        query = Product.get_query(info)
        return query.all()
