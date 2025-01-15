import { FooterApp } from "@/components/footer";
import { HeaderApp } from "@/components/header";
import { MainApp } from "@/components/main";
import {percorrerDados} from "@/components/percorrerDados";





export default function Home() {

  return (
    <div>

      <HeaderApp />

      <MainApp />

      <percorrerDados/>

      <FooterApp />

    </div>
  );
}
