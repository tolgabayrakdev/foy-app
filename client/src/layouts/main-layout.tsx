import { Text } from "@mantine/core";
import { Outlet } from "react-router-dom";

export default function MainLayout() {
    return (
        <div>
            <Text>Main Layout</Text>
            <Outlet />
        </div>
    )
}
