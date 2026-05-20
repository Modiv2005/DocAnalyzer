import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { useAuthStore } from './store/authStore';
import Login from './pages/Login';
import DashboardLayout from './layouts/DashboardLayout';
import Dashboard from './pages/Dashboard';

// Placeholder components for other routes
const Documents = () => <div className="p-6 bg-white rounded-lg shadow-sm">Documents List View coming soon...</div>;
const UploadCenter = () => <div className="p-6 bg-white rounded-lg shadow-sm">Upload Center coming soon...</div>;
const ChatAssistant = () => <div className="p-6 bg-white rounded-lg shadow-sm">AI Chat Assistant coming soon...</div>;
const RiskAnalytics = () => <div className="p-6 bg-white rounded-lg shadow-sm">Risk Analytics Dashboard coming soon...</div>;

function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const token = useAuthStore((state) => state.token);
  if (!token) return <Navigate to="/login" replace />;
  return <>{children}</>;
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        
        <Route path="/" element={<ProtectedRoute><DashboardLayout /></ProtectedRoute>}>
          <Route index element={<Dashboard />} />
          <Route path="documents" element={<Documents />} />
          <Route path="upload" element={<UploadCenter />} />
          <Route path="chat" element={<ChatAssistant />} />
          <Route path="risk" element={<RiskAnalytics />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
