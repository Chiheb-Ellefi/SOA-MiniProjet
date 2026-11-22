package tn.idl.campus;

/** Certification de formation (données fictives). */
public class Certification {
    private String code;
    private String titre;
    private String domaine;
    private String niveau;
    private int dureeHeures;
    private double prixDt;

    public Certification() { } // constructeur vide requis pour la sérialisation XML

    public Certification(String code, String titre, String domaine,
                         String niveau, int dureeHeures, double prixDt) {
        this.code = code;
        this.titre = titre;
        this.domaine = domaine;
        this.niveau = niveau;
        this.dureeHeures = dureeHeures;
        this.prixDt = prixDt;
    }

    public String getCode() { return code; }
    public void setCode(String code) { this.code = code; }
    public String getTitre() { return titre; }
    public void setTitre(String titre) { this.titre = titre; }
    public String getDomaine() { return domaine; }
    public void setDomaine(String domaine) { this.domaine = domaine; }
    public String getNiveau() { return niveau; }
    public void setNiveau(String niveau) { this.niveau = niveau; }
    public int getDureeHeures() { return dureeHeures; }
    public void setDureeHeures(int dureeHeures) { this.dureeHeures = dureeHeures; }
    public double getPrixDt() { return prixDt; }
    public void setPrixDt(double prixDt) { this.prixDt = prixDt; }
}
