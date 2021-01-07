import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.models import User as UserModel, Cart as CartModel, Product as ProductModel, Seller as SellerModel, ProductCoupon as ProductCouponModel, ProductMeta as ProductMetaModel, ProductPrice as ProductPriceModel, PrdStore as PrdStoreModel, Store as StoreModel, Address as AddressModel, StoreManager as StoreManagerModel, Buyer as BuyerModel, LocalStore as LocalStoreModel, ProductVariant as ProductVariantModel, ProductVariantType as ProductVariantTypeModel, ProductVariantTypeOption as ProductVariantTypeOptionsModel, ProductVariantOptionMap as ProductVariantOptionMapModel
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
        exclude_fields = ("created_at", "updated_at", "id", "buyer_id")


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
                          "updated_at", "prdstore")


class ProductPrice(SQLAlchemyObjectType):
    class Meta:
        model = ProductPriceModel
        exclude_fields = ("created_at", "updated_at", 'id')


class ProductSeller(SQLAlchemyObjectType):
    class Meta:
        model = PrdStoreModel
        only_fields = ('is_active', 'coupon', 'variants')


class Store(SQLAlchemyObjectType):
    class Meta:
        model = StoreModel
        exclude_fields = ("created_at", "updated_at",
                          'id', 'seller_id', 'address_id')


class Address(SQLAlchemyObjectType):
    class Meta:
        model = AddressModel
        exclude_fields = ("created_at", "updated_at", 'id')


class StoreManager(SQLAlchemyObjectType):
    class Meta:
        model = StoreManagerModel
        exclude_fields = ("created_at", "updated_at",
                          'id', 'user_id', 'store_id')


class Buyer(SQLAlchemyObjectType):
    class Meta:
        model = BuyerModel
        exclude_fields = ("created_at", "updated_at", 'id')


class LocalStore(SQLAlchemyObjectType):
    class Meta:
        model = LocalStoreModel
        exclude_fields = ("created_at", "updated_at", 'id')


class ProductVariant(SQLAlchemyObjectType):
    class Meta:
        model = ProductVariantModel
        exclude_fields = ("created_at", "updated_at", 'id')


class ProductVariantType(SQLAlchemyObjectType):
    class Meta:
        model = ProductVariantTypeModel
        exclude_fields = ("created_at", "updated_at", 'id')


class ProductVariantTypeOptions(SQLAlchemyObjectType):
    class Meta:
        model = ProductVariantTypeOptionsModel
        exclude_fields = ("created_at", "updated_at", 'id')


class ProductVariantOptionMap(SQLAlchemyObjectType):
    class Meta:
        model = ProductVariantOptionMapModel
        exclude_fields = ("created_at", "updated_at", 'id')


class Query(graphene.ObjectType):
    users = graphene.List(User)
    sellers = graphene.List(Seller)
    cart = graphene.List(Cart)
    products = graphene.List(Product)
    store = graphene.List(Store)

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

    def resolve_store(self, info):
        query = Store.get_query(info)
        return query.all()

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


schema = graphene.Schema(query=Query, types=[
                         Product, User, Cart, Seller, Store, Buyer, Address, StoreManager])
