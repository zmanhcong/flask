from market import db

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30),nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12),nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    #limit length of string, nullable=False:this is constraint, it mean NOT NULL in that column, unique=True  indicates that the Index should be created with the unique flag.(name not duplicate)


    def __repr__(self):
        return f'Item {self.name}'  #data duoc nhap tu commmand vao database -> khi ta them chuc nang này thì nó sẽ hiện tên chứ không hiện ra item.


