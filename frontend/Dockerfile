# # Use Node base image
# FROM node:18-alpine

# # Set working directory
# WORKDIR /app

# # Copy package files
# COPY package*.json ./

# # Install dependencies
# RUN npm install

# # Copy rest of files
# COPY . .

# # Build Next.js app
# RUN npm run build

# # Expose port
# EXPOSE 3000

# # Start production server
# CMD ["npm", "start"]


# ---------- BUILD STAGE ----------
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build


# ---------- PRODUCTION STAGE ----------
FROM node:18-alpine

WORKDIR /app

# Copy only required files from builder
COPY --from=builder /app ./

# Install only production dependencies
RUN npm install --omit=dev

EXPOSE 3000

CMD ["npm", "start"]