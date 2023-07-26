import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import Dashboard from "./pages/dashboard/Dashboard";
import Business from "./pages/business/Business";
import DashboardHome from "./pages/DashboardHome/DashboardHome";
import Login from "./pages/login/Login";
import Signup from "./pages/signup/Signup";
import Onboard from "./pages/onboard/Onboard";
import Company from "./pages/master/Company";
import Category from "./pages/master/Category";
import ConfigureBrand from "./pages/master/ConfigureBrand";
import AddBusiness from "./pages/business/AddBussiness";
import Store from "./pages/store/Store";
import StoreList from "./pages/store/StoreList";
import EmployeeList from "./pages/people/EmployeeList";
import EditEmployee from "./pages/people/EditEmployee";
import AddEmployee from "./pages/people/AddEmployee";
import Customer from "./pages/people/Customer";
import Supplier from "./pages/people/Supplier";
import BusinessPage from "./pages/business/BusinessPage";
import AddSale from "./pages/sale/AddSale";
import SaleList from './pages/sale/SaleList'
import Invoice from "./pages/purchase/Invoice";
import Return from "./pages/purchase/Return";
import AddInventory from "./pages/Inventory/AddInventory";
import InventoryList from "./pages/Inventory/InventoryList";
import Receipt from "./pages/accounting/Receipt";
import Payment from "./pages/accounting/Payment";

function App() {
  const isOnboard = true; // Assuming it should be initialized as true
  const isLogged = true; // Assuming it should be initialized as true
  const isSignup = true; // Assuming it should be initialized as true

  return (
    <>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route
          path="/onboarding"
          element={isOnboard ? <Navigate to='/dashboard' /> : <Onboard />}
        />
        <Route path="/dashboard" element={<Dashboard />}>
          <Route path="add_business" element={<AddBusiness />} />
          <Route path="profile" element={<Onboard />} />
          <Route path="summary" element={<DashboardHome />} />
          <Route index element={<Navigate to="summary" />} />
          <Route path="store_list" element={<StoreList />} />
          <Route path="store" element={<Store />} />
          <Route path="employee_master" element={<EmployeeList />} />
          <Route path="edit_employee/:id" element={<EditEmployee />} />
          
          <Route path="add_employee" element={<AddEmployee />} />
          <Route path="customer" element={<Customer />} />
          <Route path="supplier" element={<Supplier />} />
          <Route path="business" element={<Business />} />
          <Route path="business_page/:id" element={<BusinessPage />} />
          <Route path="company" element={<Company />}>
            <Route path="configure_brand" element={<ConfigureBrand />} />
          </Route>
          <Route path="category" element={<Category />} />
          <Route path='add_sale' element={<AddSale />} />
          <Route path='sale_list' element={<SaleList />} />
          <Route path='invoice' element={<Invoice />} />
          <Route path='return' element={<Return />} />
          <Route path="add_inventory" element={<AddInventory />} />
          <Route path="inventory_list" element={<InventoryList />} />
          <Route path='receipt' element={<Receipt />} />
          <Route path='payment' element={<Payment />} />
        </Route>
      </Routes>
    </>
  );
}

export default App;
