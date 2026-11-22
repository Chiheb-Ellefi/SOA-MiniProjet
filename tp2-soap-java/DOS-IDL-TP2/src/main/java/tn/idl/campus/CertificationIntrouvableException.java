package tn.idl.campus;

import jakarta.xml.ws.WebFault;

/** Erreur métier transmise au client sous forme de Fault SOAP. */
@WebFault(name = "CertificationIntrouvable")
public class CertificationIntrouvableException extends Exception {
    public CertificationIntrouvableException(String message) {
        super(message);
    }
}
