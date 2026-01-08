import { memo, useRef, useCallback } from 'react';
import { VncScreen, VncScreenHandle } from 'react-vnc';

interface VNCClientProps {
  wsUrl: string | null;
  isActive: boolean;
  onConnect?: () => void;
  onDisconnect?: () => void;
  onError?: (error: string) => void;
}

export const VNCClient = memo(function VNCClient({
  wsUrl,
  isActive,
  onConnect,
  onDisconnect,
  onError,
}: VNCClientProps) {
  const vncRef = useRef<VncScreenHandle>(null);

  const handleConnect = useCallback(() => {
    onConnect?.();
  }, [onConnect]);

  const handleDisconnect = useCallback(() => {
    onDisconnect?.();
  }, [onDisconnect]);

  const handleSecurityFailure = useCallback(() => {
    onError?.('Security failure');
  }, [onError]);

  if (!isActive || !wsUrl) {
    return <div className="h-full w-full bg-black" />;
  }

  return (
    <VncScreen
      ref={vncRef}
      url={wsUrl}
      scaleViewport
      background="#000000"
      style={{ width: '100%', height: '100%' }}
      onConnect={handleConnect}
      onDisconnect={handleDisconnect}
      onSecurityFailure={handleSecurityFailure}
    />
  );
});
