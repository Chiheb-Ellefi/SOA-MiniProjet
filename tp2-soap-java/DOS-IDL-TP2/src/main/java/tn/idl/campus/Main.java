package tn.idl.campus;

import jakarta.xml.ws.Endpoint;

public class Main {
    public static void main(String[] args) {
        String adresse = "http://localhost:8080/services/certifications";
        Endpoint.publish(adresse, new ServiceCertifications());
        System.out.println("Service publié : " + adresse);
        System.out.println("WSDL : " + adresse + "?wsdl");
    }
}
