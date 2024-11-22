import { useEffect, useState, ComponentType } from 'react';
import { useNavigate } from 'react-router-dom';
import { Modal, Button, Text, Group } from '@mantine/core';
import Loading from '../components/Loading';

// Props tipi için generic bir interface
interface WithAuthProps {
  // Eğer wrapped component'e özel proplar varsa buraya eklenebilir
}

function AuthProvider<P extends WithAuthProps>(WrappedComponent: ComponentType<P>) {
    const Wrapper = (props: P) => {
        const [loading, setLoading] = useState(true);
        const [accessDenied, setAccessDenied] = useState(false);
        const [showRefreshModal, setShowRefreshModal] = useState(false);
        const navigate = useNavigate();

        const refreshToken = async () => {
            try {
                const refreshResponse = await fetch("http://127.0.0.1:5000/api/auth/refresh", {
                    method: 'POST',
                    credentials: 'include',
                });

                if (refreshResponse.status === 200) {
                    return true;
                }
                return false;
            } catch (error) {
                console.error('Token refresh failed:', error);
                return false;
            }
        };

        const handleRefreshConfirm = async () => {
            setShowRefreshModal(false);
            const refreshSuccessful = await refreshToken();
            
            if (refreshSuccessful) {
                setLoading(false);
                setAccessDenied(false);
            } else {
                setLoading(false);
                setAccessDenied(true);
            }
        };

        const handleRefreshDecline = () => {
            setShowRefreshModal(false);
            setLoading(false);
            setAccessDenied(true);
        };

        useEffect(() => {
            const verifyAuthToken = async () => {
                try {
                    const res = await fetch("http://127.0.0.1:5000/api/auth/verify", {
                        method: 'GET',
                        credentials: 'include',
                    });
                    
                    if (res.status === 200) {
                        setLoading(false);
                        setAccessDenied(false);
                    } else if (res.status === 401) {
                        const data = await res.json();
                        
                        if (data.error === "Token has expired") {
                            setShowRefreshModal(true);
                        } else {
                            setLoading(false);
                            setAccessDenied(true);
                        }
                    } else {
                        setLoading(false);
                        setAccessDenied(true);
                    }
                } catch (error) {
                    console.error('Auth verification failed:', error);
                    setLoading(false);
                    setAccessDenied(true);
                }
            };
            verifyAuthToken();
        }, []);

        useEffect(() => {
            if (accessDenied && !loading) {
                navigate('/sign-in');
            }
        }, [accessDenied, loading, navigate]);

        if (loading && !showRefreshModal) {
            return <Loading />;
        }

        if (accessDenied && !showRefreshModal) {
            return null;
        }

        return (
            <>
                <Modal
                    opened={showRefreshModal}
                    onClose={handleRefreshDecline}
                    title="Oturum Süresi"
                    centered
                    closeOnClickOutside={false}
                    closeOnEscape={false}
                    withCloseButton={false}
                >
                    <Text size="sm" mb="lg">
                        Oturum süreniz doldu. Devam etmek istiyor musunuz?
                    </Text>
                    <Group justify="flex-end">
                        <Button variant="light" color="red" onClick={handleRefreshDecline}>
                            Hayır
                        </Button>
                        <Button onClick={handleRefreshConfirm}>
                            Evet
                        </Button>
                    </Group>
                </Modal>
                <WrappedComponent {...props} />
            </>
        );
    };

    return Wrapper;
}

export default AuthProvider;