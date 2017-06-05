from Test_Case.Shared_Models import Connet_Database

sql = "select * from fzaccount.b_grade where schoolId = 2488"
Connet_Database.connect_database_account(sql)