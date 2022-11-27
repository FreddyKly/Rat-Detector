<template>
    <v-app>
        <!-- App-Bar on top -->
        <v-app-bar color="teal-darken-4" elevate-on-scroll>
            <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
            <v-app-bar-title class="app_bar text-left" @click="$router.push('/')">Rat-Detector</v-app-bar-title>
            <v-spacer></v-spacer>
            <v-spacer></v-spacer>
        </v-app-bar>

        <!-- Grid with Pictures -->
        <v-main>
            <v-container fluid>
                <v-navigation-drawer v-model="drawer">
                    <v-list nav>
                        <v-list-item prepend-icon="mdi-home" title="Home" value="home" @click="$router.push('/')">
                        </v-list-item>
                        <v-list-item prepend-icon="mdi-camera-wireless " title="Sensor-Node" value="sensor-node"
                            @click="$router.push('/sensor-node')"></v-list-item>
                        <v-list-item prepend-icon="mdi-message-alert" title="Notifications" value="notifications"
                            @click="$router.push('/notifications')"></v-list-item>
                        <v-list-item prepend-icon="mdi-chart-box" title="Statistics" value="statistics"
                            @click="$router.push('/statistics')"></v-list-item>
                        <v-list-item prepend-icon="mdi-account-supervisor-circle" title="Team" value="team"
                            @click="$router.push('/team')"></v-list-item>
                    </v-list>
                </v-navigation-drawer>
                <h2>Notifications</h2>
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
export default {
    name: 'NotificationsSettings',
    data() {
        return {
            drawer: false
        };
    },
}
</script>