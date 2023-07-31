# Generated by Django 4.1.7 on 2023-07-31 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='auth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.CharField(max_length=100)),
                ('user_password', models.CharField(max_length=100, null=True)),
                ('user_ip', models.CharField(blank=True, max_length=20)),
                ('token', models.CharField(max_length=32)),
                ('token_expiry', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=20)),
                ('pin', models.CharField(max_length=6)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=10)),
                ('pan', models.CharField(max_length=10, unique=True)),
                ('gst_number', models.CharField(max_length=15)),
                ('date_of_entry', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=10, unique=True)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('adhaar', models.CharField(max_length=12, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GenBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.CharField(max_length=100)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='JwtAuth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jwt', models.CharField(max_length=300)),
                ('expiry', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ModeOfPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mop', to='POSDemo.business')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100, unique=True)),
                ('contact_number', models.CharField(max_length=10)),
                ('whatsapp_number', models.CharField(blank=True, max_length=10)),
                ('date_of_entry', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('MRP', models.CharField(max_length=20)),
                ('purchase_rate', models.CharField(max_length=20)),
                ('sale_rate', models.CharField(max_length=20)),
                ('hsn', models.CharField(blank=True, max_length=7, null=True)),
                ('quantity_type', models.CharField(choices=[('GM', 'gram'), ('PIECE', 'pieces'), ('LTR', 'litre'), ('MTR', 'meter')], max_length=5, null=True)),
                ('variable', models.BooleanField(null=True)),
                ('business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='POSDemo.business')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product', to='POSDemo.categories')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('bill_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='storeMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100)),
                ('store_location', models.CharField(max_length=200)),
                ('associated_business', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='store', to='POSDemo.business')),
                ('associated_owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='store', to='POSDemo.owner')),
            ],
        ),
        migrations.CreateModel(
            name='TaxMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VariableProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('MRP', models.CharField(max_length=20)),
                ('purchase_rate', models.CharField(max_length=20)),
                ('sale_rate', models.CharField(max_length=20)),
                ('hsn', models.CharField(blank=True, max_length=7, null=True)),
                ('quantity_type', models.CharField(choices=[('GM', 'gram'), ('PIECE', 'pieces'), ('LTR', 'litre'), ('MTR', 'meter')], max_length=5)),
                ('gst', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='variableproduct', to='POSDemo.taxmaster')),
                ('parent_product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='variableproduct', to='POSDemo.product')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionDetailsMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_entry', models.DateTimeField()),
                ('mop', models.JSONField()),
                ('products', models.JSONField()),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactiondetails', to='POSDemo.genbill')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactiondetails', to='POSDemo.business')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactiondetails', to='POSDemo.employeemaster')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactiondetails', to='POSDemo.storemaster')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_entry', models.DateTimeField()),
                ('name', models.CharField(max_length=100)),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='supplier', to='POSDemo.storemaster')),
            ],
        ),
        migrations.CreateModel(
            name='storeInventoryMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField()),
                ('available', models.CharField(max_length=100, null=True)),
                ('associated_store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='storeinventory', to='POSDemo.storemaster')),
                ('business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='storeinventory', to='POSDemo.business')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='storeinventory', to='POSDemo.product')),
            ],
        ),
        migrations.CreateModel(
            name='SalesReturnRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.CharField(max_length=100, null=True)),
                ('product', models.JSONField(null=True)),
                ('item_barcode', models.CharField(blank=True, max_length=100)),
                ('quantity_returned', models.CharField(max_length=100)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salesreturn', to='POSDemo.business')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='salesreturn', to='POSDemo.customer')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='salesreturn', to='POSDemo.employeemaster')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salesreturn', to='POSDemo.storemaster')),
            ],
        ),
        migrations.CreateModel(
            name='SalesRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.CharField(max_length=100, null=True)),
                ('item_barcode', models.CharField(blank=True, max_length=100)),
                ('product_quantity', models.CharField(max_length=100)),
                ('mrp', models.CharField(max_length=50, null=True)),
                ('purchase_rate', models.CharField(max_length=50, null=True)),
                ('sale_rate', models.CharField(max_length=20, null=True)),
                ('bill_ID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salesregister', to='POSDemo.genbill')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salesregister', to='POSDemo.business')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='salesregister', to='POSDemo.customer')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='salesregister', to='POSDemo.employeemaster')),
                ('gst', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salesregister', to='POSDemo.taxmaster')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='salesregister', to='POSDemo.product')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salesregister', to='POSDemo.storemaster')),
            ],
        ),
        migrations.CreateModel(
            name='SalesPending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_quantity', models.CharField(max_length=20)),
                ('product_name', models.CharField(max_length=100)),
                ('mrp', models.CharField(max_length=20, null=True)),
                ('purchase_rate', models.CharField(max_length=20)),
                ('sale_rate', models.CharField(max_length=20)),
                ('row_total', models.CharField(max_length=20)),
                ('bill_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='salespending', to='POSDemo.genbill')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salespending', to='POSDemo.business')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='salespending', to='POSDemo.customer')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salespending', to='POSDemo.employeemaster')),
                ('gst', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salespending', to='POSDemo.taxmaster')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salespending', to='POSDemo.product')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salespending', to='POSDemo.storemaster')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField()),
                ('purchase_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mrp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='POSDemo.business')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='POSDemo.storemaster')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('permissions', models.ManyToManyField(related_name='roles', to='POSDemo.permission')),
            ],
        ),
        migrations.CreateModel(
            name='ReturnTransactionDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.CharField(max_length=100)),
                ('date_of_entry', models.DateTimeField()),
                ('amount', models.CharField(max_length=100, null=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='returntransaction', to='POSDemo.business')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='returntransaction', to='POSDemo.employeemaster')),
                ('mop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='returntransactiondetails', to='POSDemo.modeofpayment')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='returntransaction', to='POSDemo.storemaster')),
            ],
        ),
        migrations.CreateModel(
            name='ReturnSalesPending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_entry', models.DateTimeField()),
                ('return_quantity', models.CharField(max_length=50, null=True)),
                ('bill_ID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='returnsalespending', to='POSDemo.genbill')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='returnsalespending', to='POSDemo.business')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='returnsalespending', to='POSDemo.customer')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='returnsalespending', to='POSDemo.employeemaster')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='returnsalespending', to='POSDemo.product')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='returnsalespending', to='POSDemo.storemaster')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseTransactionDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.CharField(max_length=100, null=True)),
                ('date_of_entry', models.DateTimeField()),
                ('mop', models.JSONField()),
                ('supplier_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='purchasetransaction', to='POSDemo.suppliermaster')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.CharField(max_length=100, null=True)),
                ('date_and_time', models.DateTimeField()),
                ('quantity', models.CharField(max_length=20)),
                ('purchase_rate', models.CharField(max_length=100, null=True)),
                ('total', models.CharField(max_length=100, null=True)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='purchaseregister', to='POSDemo.product')),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='purchaseregister', to='POSDemo.storemaster')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='prchaseregister', to='POSDemo.suppliermaster')),
            ],
        ),
        migrations.CreateModel(
            name='PurchasePending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_and_time', models.DateTimeField(null=True)),
                ('quantity', models.CharField(max_length=20)),
                ('purchase_rate', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100, null=True)),
                ('products', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='purchasepending', to='POSDemo.product')),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='purchasepending', to='POSDemo.storemaster')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='purchasepending', to='POSDemo.suppliermaster')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='gst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='product', to='POSDemo.taxmaster'),
        ),
        migrations.CreateModel(
            name='OwnerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=20)),
                ('pin', models.CharField(max_length=6)),
                ('country', models.CharField(max_length=20)),
                ('pan_card_number', models.CharField(max_length=10, unique=True)),
                ('date_of_entry', models.DateField()),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='details', to='POSDemo.owner')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField()),
                ('action', models.CharField(choices=[('A', 'added'), ('R', 'removed')], max_length=1)),
                ('quantiy', models.CharField(max_length=100)),
                ('reason', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='inventorymanager', to='POSDemo.product')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='inventorymanager', to='POSDemo.storemaster')),
            ],
        ),
        migrations.AddField(
            model_name='genbill',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bill', to='POSDemo.storemaster'),
        ),
        migrations.CreateModel(
            name='EmployeeCredential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, null=True, unique=True)),
                ('password', models.CharField(max_length=100, unique=True)),
                ('modified_on', models.DateTimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='credential', to='POSDemo.employeemaster')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeAuth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jwt', models.CharField(max_length=300)),
                ('have_access', models.BooleanField()),
                ('business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='employee_auth', to='POSDemo.business')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='authentication', to='POSDemo.employeemaster')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_of_entry', models.TimeField()),
                ('time_of_relief', models.TimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='attendance', to='POSDemo.employeemaster')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='employeeAttendance', to='POSDemo.storemaster')),
            ],
        ),
        migrations.CreateModel(
            name='Daily_employee_management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('designation', models.CharField(max_length=100)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='dailymanager', to='POSDemo.employeemaster')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='dailymanager', to='POSDemo.storemaster')),
            ],
        ),
        migrations.AddField(
            model_name='categories',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='POSDemo.storemaster'),
        ),
        migrations.CreateModel(
            name='BusinessInventoryMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField()),
                ('available', models.CharField(max_length=20)),
                ('associated_business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='POSDemo.business')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='businessinventory', to='POSDemo.product')),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='owner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='business', to='POSDemo.owner'),
        ),
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=50)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='barcode', to='POSDemo.product')),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='barcode', to='POSDemo.storemaster')),
            ],
        ),
    ]
