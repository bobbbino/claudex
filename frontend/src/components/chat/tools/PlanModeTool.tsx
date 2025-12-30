import { memo } from 'react';
import { Map } from 'lucide-react';
import type { ToolAggregate } from '@/types';
import { ToolCard } from './common';

const EnterPlanModeInner: React.FC<{ tool: ToolAggregate }> = ({ tool }) => (
  <ToolCard
    icon={<Map className="h-3.5 w-3.5 text-text-secondary dark:text-text-dark-tertiary" />}
    status={tool.status}
    title="Enter plan mode"
    loadingContent="Entering plan mode..."
    error={tool.error}
  />
);

const ExitPlanModeInner: React.FC<{ tool: ToolAggregate }> = ({ tool }) => (
  <ToolCard
    icon={<Map className="h-3.5 w-3.5 text-text-secondary dark:text-text-dark-tertiary" />}
    status={tool.status}
    title="Exit plan mode"
    loadingContent="Exiting plan mode..."
    error={tool.error}
  />
);

export const EnterPlanModeTool = memo(EnterPlanModeInner);
export const ExitPlanModeTool = memo(ExitPlanModeInner);
