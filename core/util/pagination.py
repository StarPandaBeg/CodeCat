class Pagination:
    def __init__(self, page: int = 1, perPage: int = 10):
        self.page = page
        self.perPage = 10
        self.stmt = None
        self.cache = {}

    @property
    def offset(self):
        return (self.page - 1) * self.perPage

    @property
    def total_pages(self):
        total = self.total()
        last = total % self.perPage
        return (total // self.perPage) + (1 if last > 0 else 0)

    def set_stmt(self, stmt):
        self.stmt = stmt

    def paginate(self, force=False):
        if 'paginated' in self.cache and not force:
            return self.cache['paginated']
        obj = self.stmt.limit(self.perPage).offset(self.offset).all()
        self.cache['paginated'] = obj
        return obj

    def total(self, force=False):
        if 'total' in self.cache and not force:
            return self.cache['total']
        obj = self.stmt.count()
        self.cache['total'] = obj
        return obj
