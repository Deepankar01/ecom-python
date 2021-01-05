import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.models import User as UserModel, Cart as CartModel, Product as ProductModel, Seller as SellerModel, ProductCoupon as ProductCouponModel, ProductMeta as ProductMetaModel, ProductPrice as ProductPriceModel, PrdSeller as PrdSellerModel
from sqlalchemy.orm import class_mapper
from sqlalchemy.sql import or_

class_mapper(UserModel)


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


class ProductMeta(SQLAlchemyObjectType):
    class Meta:
        model = ProductMetaModel
        exclude_fields = ("created_at", "updated_at", 'id')


class ProductCoupon(SQLAlchemyObjectType):
    class Meta:
        model = ProductCouponModel
        exclude_fields = ('prd_seller_id', 'id', "created_at",
                          "updated_at", "prdseller")


class ProductPrice(SQLAlchemyObjectType):
    class Meta:
        model = ProductPriceModel
        exclude_fields = ("created_at", "updated_at", 'id')


class ProductSeller(SQLAlchemyObjectType):
    class Meta:
        model = PrdSellerModel
        only_fields = ('is_active', 'coupon')


class Query(graphene.ObjectType):
    users = graphene.List(User)
    sellers = graphene.List(Seller)
    cart = graphene.List(Cart)
    products = graphene.List(Product)

    product_by_id = graphene.Field(Product, id=graphene.UUID())
    product_by_text = graphene.List(Product, search=graphene.String())

    @staticmethod
    def resolve_product_by_text(parent, info, **args):
        q = args.get('search')
        products_query = Product.get_query(info)
        return products_query.filter(or_(ProductModel.title.contains(q), ProductModel.description.contains(q))).all()

    @staticmethod
    def resolve_product_by_id(parent, info, **args):
        q = args.get('id')
        products_query = Product.get_query(info)
        return products_query.get(q)

    def resolve_users(self, info):
        query = User.get_query(info)
        return query.all()

    def resolve_sellers(self, info):
        query = Seller.get_query(info)
        return query.all()

    def resolve_cart(self, info):
        query = Cart.get_query(info)
        return query.all()

    def resolve_products(self, info):
        query = Product.get_query(info)
        return query.all()


schema = graphene.Schema(query=Query, types=[Product, User, Cart, Seller])
