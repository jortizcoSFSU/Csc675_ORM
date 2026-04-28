"""
    This file will implement the base code to create relationships between tables,
    For example, getting all the reviews' model instances from a specific product model

    Note: we will implement this file in class in the ORM demo lecture

    For this implementation of the Relation class we are going to use this example

    track7 = Track.get(id=7)
    # relation
    album = track7.album



"""
class Relation:
    """
    We are going to implement this class in three phases:
    (1) basic relation
    (2) Lazy loading
    (3) backreferences

    album_object = Relation(model_name='Album', foreign_key='album_id')
    """

    def __init__(self, model_name, foreign_key, backreference=None, lazy_load=True):
        self.model_name = model_name
        self.fk = foreign_key
        self.lazy = lazy_load
        self.attribute_name = None # album_object (the name not the model)
        self.backreference = backreference


    def __set_name__(self, owner, name):
        self.attribute_name = name


    def __get__(self, instance, owner):
        """
        Imagine track7 = Track.get(id=7)
                album = track7.album # album with id 5
        :param instance: track
        :param owner: Track
        :return:
        """
        if instance is None:
            return self

        # check if the model object can be retrieved from the cache
        cache = Cache(self.attribute_name)
        if self.lazy:
            if cache.has(instance):
                return cache.get(instance) # found the model object in the cache


        # Track.resolve_model['Album'] # owner
        # track.resolve_model['Album'] # instance
        model = owner.resolve_model(self.model_name)
        fk_value = getattr(instance, self.fk)

        if model is None or fk_value is None:
            return None

        # We know that the model object is not in the cache
        # then we need to retrieve this from the database

        model_obj = model.get(fk_value)

        if self.lazy and cache is not None:
            cache.add(instance, model_obj)


        # album = track.album
        # track = album.track --> this
        setattr(model_obj, self.backreference, instance)

        return model_obj


class Cache:
    """
    Will allow lazy loading, once an instance of a model is retrieved from
    the database for the first time, after that it will be stored in the cache
    and next time we need it, it will be retrieved from the Cache.
    """

    def __init__(self, attribute_name):
        self.cache_name = f"_{attribute_name}_cache"

    @property
    def name(self):
        return self.cache_name

    def add(self, instance, model_object):
        """
        {instance, cache_name, album}
        :param instance: track
        :param model_object: album
        :return:
        """
        setattr(instance, self.cache_name, model_object)

    def get(self, instance):
        return getattr(instance, self.cache_name)

    def has(self, instance):
        return hasattr(instance, self.cache_name)























