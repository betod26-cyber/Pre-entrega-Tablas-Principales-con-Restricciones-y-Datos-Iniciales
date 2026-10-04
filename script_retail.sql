-- ============================================================================
-- ENTREGABLE: SCRIPT DE BASE DE DATOS - RETAIL PROJECT
-- OBJETIVO: Crear estructura DDL, restricciones CHECK, control de transacciones
--           y manipulación de datos (DML).
-- ============================================================================

-- 1. CREACIÓN DE LA BASE DE DATOS
-- Nota: En la mayoría de los gestores, este comando se ejecuta por separado.
CREATE DATABASE retail_project;

-- (Asegúrate de conectarte a 'retail_project' antes de ejecutar lo siguiente)

-- ============================================================================
-- BLOQUE DDL: CREACIÓN DE TABLAS Y RESTRICCIONES
-- ============================================================================

-- Creación de la tabla Clientes
CREATE TABLE clientes (
    cliente_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    edad INT NOT NULL,
    ciudad VARCHAR(50),
    -- Restricción CHECK 1: La edad del cliente debe ser razonable y mayor de edad para compras
    CONSTRAINT chk_edad_cliente CHECK (edad >= 18 AND edad <= 120)
);

-- Creación de la tabla Productos
CREATE TABLE productos (
    producto_id SERIAL PRIMARY KEY,
    nombre_producto VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    precio_unitario NUMERIC(10, 2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    -- Restricción CHECK 2: El precio unitario debe ser estrictamente mayor a cero
    CONSTRAINT chk_precio_positivo CHECK (precio_unitario > 0.00)
);

-- Creación de la tabla Ventas
CREATE TABLE ventas (
    venta_id SERIAL PRIMARY KEY,
    cliente_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad_vendida INT NOT NULL,
    fecha_venta DATE NOT NULL DEFAULT CURRENT_DATE,
    -- Claves Foráneas (Integridad Referencial)
    CONSTRAINT fk_ventas_clientes FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id) ON DELETE CASCADE,
    CONSTRAINT fk_ventas_productos FOREIGN KEY (producto_id) REFERENCES productos(producto_id) ON DELETE RESTRICT,
    -- Restricción CHECK 3: La cantidad vendida debe ser al menos 1 producto
    CONSTRAINT chk_cantidad_vendida CHECK (cantidad_vendida > 0)
);

-- ============================================================================
-- BLOQUE TRANSACTION: CARGA masiva de DATOS CONTROLADA
-- ============================================================================
BEGIN;

-- Insertar 5 registros en la tabla clientes
INSERT INTO clientes (nombre, email, edad, ciudad) VALUES
('Juan Pérez', 'juan.perez@email.com', 28, 'Buenos Aires'),
('María García', 'maria.garcia@email.com', 34, 'Rosario'),
('Carlos López', 'carlos.lopez@email.com', 45, 'Córdoba'),
('Ana Martínez', 'ana.martinez@email.com', 22, 'Mendoza'),
('Luis Rodríguez', 'luis.rodriguez@email.com', 51, 'Tucumán');

-- Insertar 5 registros en la tabla productos
INSERT INTO productos (nombre_producto, categoria, precio_unitario, stock) VALUES
('Notebook Pro 15', 'Tecnología', 1200.00, 15),
('Mouse Ergonómico', 'Tecnología', 45.50, 50),
('Teclado Mecánico RGB', 'Tecnología', 89.99, 30),
('Escritorio Reclinable', 'Mobiliario', 350.00, 10),
('Silla Gamer Premium', 'Mobiliario', 250.00, 20);

-- Insertar 5 registros en la tabla ventas (asociando IDs existentes)
INSERT INTO ventas (cliente_id, producto_id, cantidad_vendida, fecha_venta) VALUES
(1, 1, 1, '2026-09-15'), -- Juan compra una Notebook
(2, 2, 2, '2026-09-16'), -- María compra dos Mouse
(3, 4, 1, '2026-09-18'), -- Carlos compra un Escritorio
(4, 3, 1, '2026-09-20'), -- Ana compra un Teclado
(5, 5, 1, '2026-09-21'); -- Luis compra una Silla

COMMIT;
-- ============================================================================


-- ============================================================================
-- BLOQUE DML: MODIFICACIÓN Y ELIMINACIÓN DE DATOS PRECISOS
-- ============================================================================

-- Sentencia UPDATE: Modifica el precio incrementando un 10% a toda la categoría 'Tecnología'
UPDATE productos
SET precio_unitario = precio_unitario * 1.10
WHERE categoria = 'Tecnología';

-- Sentencia DELETE: Elimina de forma específica la venta con ID 3 usando WHERE preciso
DELETE FROM ventas
WHERE venta_id = 3;
