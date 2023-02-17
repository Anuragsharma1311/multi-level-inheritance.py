class grandfather:
      def details(self):
          print('i am a grandfather')

class father(grandfather):
    def detailss(self):
        print('i am a parent')

class grandchild(father):
    def detailsss(self):
        print('i am a grandchild')

mummy=grandchild()
mummy.details()
mummy.detailss()
mummy.detailsss()

