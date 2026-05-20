import React from 'react';
import { useQuery } from '@tanstack/react-query';
import api from '../api/axios';
import { FileText, ShieldAlert, CheckCircle, Activity } from 'lucide-react';

export default function Dashboard() {
  const { data: stats, isLoading } = useQuery({
    queryKey: ['dashboard-stats'],
    queryFn: async () => {
      const res = await api.get('/analytics/dashboard');
      return res.data;
    }
  });

  if (isLoading) {
    return <div className="flex justify-center items-center h-64"><div className="animate-spin rounded-full h-8 w-8 border-b-2 border-brand-600"></div></div>;
  }

  const statCards = [
    { name: 'Total Documents', value: stats?.total_documents || 0, icon: FileText, color: 'text-blue-600', bg: 'bg-blue-100' },
    { name: 'Processed Documents', value: stats?.processed_documents || 0, icon: CheckCircle, color: 'text-green-600', bg: 'bg-green-100' },
    { name: 'Risks Identified', value: stats?.total_risks_identified || 0, icon: ShieldAlert, color: 'text-red-600', bg: 'bg-red-100' },
    { name: 'Clauses Extracted', value: stats?.total_clauses_extracted || 0, icon: Activity, color: 'text-purple-600', bg: 'bg-purple-100' },
  ];

  return (
    <div className="space-y-6">
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
        {statCards.map((item) => (
          <div key={item.name} className="bg-white overflow-hidden shadow-sm rounded-lg border border-gray-100">
            <div className="p-5">
              <div className="flex items-center">
                <div className="flex-shrink-0">
                  <div className={`p-3 rounded-md ${item.bg}`}>
                    <item.icon className={`h-6 w-6 ${item.color}`} aria-hidden="true" />
                  </div>
                </div>
                <div className="ml-5 w-0 flex-1">
                  <dl>
                    <dt className="text-sm font-medium text-gray-500 truncate">{item.name}</dt>
                    <dd>
                      <div className="text-2xl font-semibold text-gray-900">{item.value}</div>
                    </dd>
                  </dl>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className="bg-white shadow-sm rounded-lg border border-gray-100 p-6 mt-8">
        <h3 className="text-lg font-medium text-gray-900 mb-4">Recent Activity</h3>
        <div className="text-center py-12 text-gray-500">
          Upload some documents to see recent activity.
        </div>
      </div>
    </div>
  );
}
