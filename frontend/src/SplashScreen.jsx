import animation from "./assets/Jarvis_interface.webp";

function SplashScreen() {
  return (
    <div style={styles.container}>
      <img src={animation} alt="loading" style={styles.image} />
    </div>
  );
}

const styles = {
  container: {
    position: "fixed",
    top: 0,
    left: 0,
    width: "100vw",
    height: "100vh",
    backgroundColor: "#000",
    zIndex: 9999,
  },
  image: {
    width: "100%",
    height: "100%",
    objectFit: "cover", // 🔥 ÇA c’est la clé du full screen
  },
};

export default SplashScreen;
