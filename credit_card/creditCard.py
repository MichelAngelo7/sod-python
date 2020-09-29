class CreditCard:
    def __init__(self,user, dateOfPurchase, creditorCompany=None,
                 numberOfInstallments=0, InstallmentsValue=0, category=None):
        self.user
        self.dateOfPurchase = dateOfPurchase
        self.creditorCompany = creditorCompany
        self.numberOfInstallments = numberOfInstallments
        self.category = category
        self.purchases = []

    def register_purchases(self, purchases):
        self.purchases.append(purchases)

    def __str__(self):
        return f'Data da compra: {self.dateOfPurchase} \
          Nome da empresa: {self.creditorCompany} \
          Número de parcelas {self.numberOfInstallments}\
          Categoria: {self.category} '
